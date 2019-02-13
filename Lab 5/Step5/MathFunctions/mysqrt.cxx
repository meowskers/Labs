#include "MathFunctions.h"
#include <iostream>
#include <math.h>

// a hack square root calculation using simple operations
double mysqrt(double x)
{
  // if we have both log and exp then use them
  #if defined(HAVE_LOG) && defined (HAVE_EXP)
    double result = exp(log(x)*0.5);
    std::cout << "Computing sqrt of " << x << " to be " << result << " using log" << std::endl;
  #else
  if (x <= 0) {
    return 0;
  }

  double result = x;

  // do ten iterations
  for (int i = 0; i < 10; ++i) {
    if (result <= 0) {
      result = 0.1;
    }
    double delta = x - (result * result);
    result = result + 0.5 * delta / result;
    std::cout << "Computing sqrt of " << x << " to be " << result << std::endl;
  }
  return result;
}
