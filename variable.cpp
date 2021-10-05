#include<iostream>
#include<fstream>
using namespace std;
ifstream in("speed.in");
ofstream out("speed.txt");
int main()
{
    float speed_combined, upload_speed, download_speed;
    in>>upload_speed;
    in>>download_speed;
    download_speed = download_speed * 100;
    download_speed = (int) download_speed;
    download_speed = download_speed / 100.0;

    upload_speed = upload_speed * 100;
    upload_speed = (int) upload_speed;
    upload_speed = upload_speed / 100.0;
    
    speed_combined = upload_speed + download_speed;
    out<<speed_combined<<"\n"<<upload_speed<<"\n"<<download_speed;
}