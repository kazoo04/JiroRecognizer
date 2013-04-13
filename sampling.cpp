#include <iostream>
#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/features2d/features2d.hpp>
#include "opencv2/nonfree/nonfree.hpp"

#pragma comment(lib,"opencv_nonfree242.lib")

int main(int argc, char* argv[])
{
    //std::cout << CV_VERSION << std::endl; 

    cv::Mat img = cv::imread(argv[1]);
    if (img.empty()) {
        exit(EXIT_FAILURE);
    }

    double r = 32.0f;     //radius of feature point
    double interval = 30;   //feature interval

    //cv::DenseFeatureDetector detector(r, 1, 0.1f, interval);
    cv::DenseFeatureDetector detector(
            8.0f,   //initFeatureScale: 初期の特徴のサイズ（半径）
            4,      //featureScaleLevels: 何段階サイズ変更してしてサンプリングするか(>=1)
            1.414f, //featureScaleMul:  ScaleLevelごとにどれくらい拡大縮小するか(!=0)
            4,      //initXyStep: 特徴点をどれくらいの量ずらしながらサンプリングするか
            0,      //initImgBound: 画像の端からどれくらい離すか(>=0)
            false,  //varyXyStepWithScale: XyStepにもScaleMul を掛けるか
            false   //varyImgBoundWithScale: BoundにもScaleMul を掛けるか
    );

    std::vector<cv::KeyPoint> keypoints;
    detector.detect(img, keypoints);

    cv::SiftDescriptorExtractor extractor(3.0, true, false);
    cv::Mat descriptors;
    extractor.compute(img, keypoints, descriptors);

    std::cout << cv::format(descriptors, "csv") << std::endl;

    /*
    detector.detect(img, keypoints);

    std::vector<cv::KeyPoint>::iterator it;
    for (it = keypoints.begin(); it != keypoints.end(); it++) {
        std::cout << it->pt << std::endl;
        cv::circle(img, it->pt, it->size, cv::Scalar(0, 255, 255), 1, CV_AA);
        cv::circle(img, it->pt, 1, cv::Scalar(0,255,0), -1);
    }

    cv::namedWindow("result", CV_WINDOW_AUTOSIZE);
    cv::imshow("result", img);
    cv::waitKey();
    */

    return 0;
}
