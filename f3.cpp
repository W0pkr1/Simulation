#pragma once
#include "integrators.cpp"


void simulation_3(int const& steps, float const& h, float const& a, float const& b, float const& c, float const& d)
{  
    std::ofstream output("data/f3/end.txt");
    output<<"nr nf t"<<std::endl;
    
    unsigned int nr = 100;
    unsigned int nf = 100;
    auto f1 = [&a, &b, &nf](float nr) {return a * nr - b*nf * nr; };
    auto f2 = [&d, &c, &nr](float nf) {return c*nr * nf - d * nf; };

    float t = 0.f;

    for (int i = 0; i < steps; ++i)
    {

        float res1 =  integrator_rungekutta(f1, nr, h);
        float res2 =  integrator_rungekutta(f2, nf, h);
        
        nr +=(unsigned int) res1;
        nf +=(unsigned int) res2;
        t += h;
        
        output<<nr<<' '<<nf<<' '<<t<<std::endl;
    }
    output.close();

}