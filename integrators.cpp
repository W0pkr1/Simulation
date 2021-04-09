#pragma once

#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>
#include <string>


template <typename F>
float integrator_euler(F func, float const &  x, float const & h)
{
    return func(x)*h;
}

template <typename F>
float integrator_rungekutta(F func, float const & x, float const & h)
{
    
    float k1 = func(x);
    float k2 = func(x+k1/2);
    float k3 = func(x+k2/2);
    float k4 = func(x+k3);
    float result = (k1 + 2 * k2 + 2 * k3 + k4);
    result /= 6;

    return result;
    

}