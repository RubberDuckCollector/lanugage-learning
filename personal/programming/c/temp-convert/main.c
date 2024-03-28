#include <stdio.h>

int f_to_c(int f) {
  /* celcius = (5/9)(fahrenheit - 32) */
  /* we can times everything by the numerator 5 then divide everything by the
   * denominator 9 */
  /* since we're multiplying everything else by the fraction 5/9 */
  int c;

  c = 5 * (f - 32) / 9;

  return c;
}

float f_to_c_float(float f) {
  float c;

  // we can immediately use floats in our mathematics
  // additionally, using floats allows us to multiply by the fraction outright
  // instead of multiplying by numerator then dividing by denominator
  c = (5.0 / 9.0) * (f - 32.0);

  return c;
}

int main() {
  printf("integer division\n");
  for (int i = 0; i < 301; i += 20) {
    printf("%3d\t%6d\n", i, f_to_c(i));
  }

  printf("division with floats\n");
  for (float i = 0.0; i < 301.0; i += 20.0) {
    printf("%3.0f\t%6.1f\n", i, f_to_c_float(i));
  }

  return 0;
}
