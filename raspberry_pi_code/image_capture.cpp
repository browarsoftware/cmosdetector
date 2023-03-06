#include <opencv2/core.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/opencv.hpp>
#include <iostream>
#include <stdio.h>
#include <sys/timeb.h>
using namespace cv;
using namespace std;


Mat convertTo32F(Mat frame, float *image_sum_ptr)
{
	int end_row = frame.rows;
	int end_col = frame.cols;
	if (image_sum_ptr == NULL)
		image_sum_ptr = new float[end_row * end_col];
    unsigned char *frame_ptr = (unsigned char*)frame.data;
	float b, g, r;
	int step = frame.step;
	int channels = frame.channels();
	float max_help;
	int addr = 0;
	int image_sum_addr = 0;
	for(int j = 0;j < end_row;j++){
	    for(int i = 0;i < end_col;i++){
			image_sum_addr = end_col * j + i;
			addr = (step * j) + (i * channels);

			b = frame_ptr[addr] ;
			g = frame_ptr[addr + 1];
			r = frame_ptr[addr + 2];
			
			max_help = b + g + r;
			
			image_sum_ptr[image_sum_addr] = max_help;
	    }
	}
	
	Mat image_sum = Mat(end_row, end_col, CV_32F, image_sum_ptr);
	return image_sum;
}

Mat maxPooling2_32F(Mat frame, float *image_pool_ptr)
{
	int end_col = frame.cols;
	
	int end_row_half = frame.rows / 2;
	int end_col_half = frame.cols / 2;
	
	if (image_pool_ptr == NULL)
		image_pool_ptr = new float[end_row_half * end_col_half];
	float *frame_ptr = (float*)frame.data;

	float max_help;

	int image_sum_addr = 0;
	float id00, id01, id10, id11;
	for(int j = 0;j < end_row_half;j++){
	    for(int i = 0;i < end_col_half;i++){
			image_sum_addr = end_col_half * j + i;
			
			id00 = frame_ptr[(end_col * 2 * j) + (2 * i)];
		    id01 = frame_ptr[(end_col * 2 * j) + (2 * i + 1)];
		    id10 = frame_ptr[(end_col * (2 * j + 1)) + (2 * i)];
		    id11 = frame_ptr[(end_col * (2 * j + 1)) + (2 * i + 1)];
			
			max_help = id00;
			if (max_help < id01)
				max_help = id01;
			if (max_help < id10)
				max_help = id10;
			if (max_help < id11)
				max_help = id11;
			
			image_pool_ptr[image_sum_addr] = max_help;
	    }
	}
	
	Mat image_sum = Mat(end_row_half, end_col_half, CV_32F, image_pool_ptr);
	return image_sum;
}


int main(int, char**)
{
    // Start and end times
    time_t start, end;
    double fps = 0;
    double max_sec = 60;
    Mat frame;
    //--- INITIALIZE VIDEOCAPTURE
    VideoCapture cap;
    int deviceID = 0;             // 0 = open default camera
    int apiID = cv::CAP_ANY;      // 0 = autodetect default API
    // open selected camera using selected API
    cap.open(deviceID, apiID);
    // check if we succeeded
    if (!cap.isOpened()) {
        cerr << "ERROR! Unable to open camera\n";
        return -1;
    }
    cap.set(CV_CAP_PROP_FRAME_WIDTH,1920);
    cap.set(CV_CAP_PROP_FRAME_HEIGHT,1080);
      
    //--- GRAB AND WRITE LOOP
    cout << "Start grabbing" << endl
        << "Press any key to terminate" << endl;
        
    // Start time
    time(&start);

    Size kernelSize = Size(3, 3);

    Mat image2, image_sum, image_blur, avg_image, image_diff;
    int calculate_mean = 100;
    bool first = true;
    
    float fraction = 0.8;
    float fractionMinus = 1.0f - fraction;
    
    std::string name_hist_255 = "./data_history_pooling/treHistory255/";
    std::string extension = ".png";
    std::string result;
    int id_tr = 0;
    int id_hist = 0;
    
    int end_row = 0;
    int end_col = 0;
    int i, j, id_arr;

    Mat frame1;
    
    float* image_frame_to_32f_ptr = new float[(1920 - 60) * (1080 - 60)];
    
    
    int end_row_half = (1920 - 60) / 2;
    int end_col_half = (1080 - 60) / 2;
    
    float *avg_image_ptr = new float[end_row_half * end_col_half];
	
    float *image_pool_ptr = new float[end_row_half * end_col_half];
    
    float *image_sum_ptr;

    Rect crop(30,30, 1920 - 60, 1080 - 60);
    
    float *image_blur_ptr;
    
    for (;;)
    {
        // wait for a new frame from camera and store it into 'frame'
        cap.read(frame);
		// check if we succeeded
        if (frame.empty()) {
            cerr << "ERROR! blank frame grabbed\n";
            break;
        }
	Mat crop_me = frame(crop);
	

	Mat crop_me32f = convertTo32F(crop_me, image_frame_to_32f_ptr);
	Mat image_pool = maxPooling2_32F(crop_me32f, image_pool_ptr);
	
	GaussianBlur(image_pool, image_blur, kernelSize, 0);
	
	if (calculate_mean <= 0)
	{    
	    image_blur_ptr = (float*)(image_blur.data);
	    image_sum_ptr = (float*)(image_pool.data);	    
	    
	    end_row = image_blur.rows;
	    end_col = image_blur.cols;
	    
	    for(j = 0; j < end_row; j++){
		for(i = 0; i < end_col; i++){
		    id_arr = end_col * j + i;
		    
		    if (avg_image_ptr[id_arr] * 4.0 < image_blur_ptr[id_arr] 
			&& image_sum_ptr[id_arr] > 255)
		    {
			result = name_hist_255 + std::to_string(id_hist) + " " 
			    + std::to_string((int)image_sum_ptr[id_arr]) + " " +  std::to_string((double)(4.0 * avg_image_ptr[id_arr])) + " " +  std::to_string((double)image_blur_ptr[id_arr] ) + extension;
			cout << result << endl;
			id_hist++;
			imwrite(result, frame);
		    }		    
		}
	    }
	}
	else
	{
	    calculate_mean--;
	}
	if (first)
	{
	    first = false;
	    image_blur_ptr = (float*)(image_blur.data);
	    
	    end_row = image_blur.rows;
	    end_col = image_blur.cols;

	    for(j = 0; j < end_row; j++){
		for(i = 0; i < end_col; i++){
		    id_arr = end_col * j + i;
		    avg_image_ptr[id_arr] = image_blur_ptr[id_arr];
		}
	    }
	}
	else
	{
	    image_blur_ptr = (float*)(image_blur.data);
	    
	    
	    end_row = image_blur.rows;
	    end_col = image_blur.cols;
	    
	    for(j = 0; j < end_row; j++){
		for(i = 0; i < end_col; i++){
		    id_arr = (end_col * j) + i;
		    avg_image_ptr[id_arr] = (fractionMinus * avg_image_ptr[id_arr]) + (fraction * image_blur_ptr[id_arr]);
		}
	    }
	}
	
	time(&end);
	double seconds = difftime(end, start);
	fps++;
	if (seconds > max_sec)
	{
	    cout << fps / seconds << endl;
	    
	    if (fps / seconds < 2.5)
	    {
		return 42;
		cout << "Restarting camera!" << endl;
		cap.release();
	    }
	    
	    fps = 0;
	    time(&start);
	}

    }
    delete []avg_image_ptr;
    delete []image_pool_ptr;
    delete []image_frame_to_32f_ptr;
    
    // the camera will be deinitialized automatically in VideoCapture destructor
    return 0;
}
