#pragma once
#include "integrators.cpp"


void simulation_2(int const& steps,float const& h,float const& r1,float const& r2,
float const& a, float const & b, float const& k1, float const& k2)
{  
    std::ofstream output("data/f2/outs.txt");
    output<<"n1 n2 t"<<std::endl;
    
    float n1 = .4;
    float n2 = .4;

    auto f1 = [&a,&r1,&k1,&n2] (float n1) {return r1*n1*(1-((n1+a*n2)/k1));};
    auto f2 = [&b,&r2,&k2,&n1] (float n2) {return r2*n2*(1-((n2+b*n1)/k2));};
    
    float t = 0.f;

    for (int i = 0; i < steps; ++i)
    {
        float res1 =  integrator_rungekutta(f1, n1, h);
        float res2 =  integrator_rungekutta(f2, n2, h);
        
        n1 += res1;
        n2 += res2;
        t += h;
        
        output<<n1<<' '<<n2<<' '<<t<<std::endl;
    }
    output.close();

}