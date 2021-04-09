#pragma once
#include "integrators.cpp"


void simulation_1(int const& steps,float const& h,float const& r)
{  
    std::ofstream output("data/f1/"+std::to_string(r)+".txt");
    output<<"euler runge t"<<std::endl;

    auto f = [&r](float x) {return r * x * (1-x); };

    float t = 0.f;
    float x_e = 0.;
    float x_k = 0.;

    for (int i = 0; i < steps; ++i)
    {
        x_e += integrator_euler(f, x_e, h);
        x_k += integrator_rungekutta(f, x_k, h);
        
        t += h;
        output<<x_e<<' '<<x_k<<' '<<t<<std::endl;
    }
    output.close();

}