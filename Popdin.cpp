
#include "f1.cpp"
#include "f2.cpp"
#include "f3.cpp"
int main()
{
    std::vector<float> r_s = {1.f,.5f,0.f,-.5f,-1.f};
    for(auto r:r_s)
    {
        simulation_1(100,1,r);
    }
    simulation_2(100, 1, .4, .4, 0.4, 0.4, 0.2, 0.8);
    simulation_3(100, 1, 0.2, 0.00002, 0.000025, 0.80);

    

}

