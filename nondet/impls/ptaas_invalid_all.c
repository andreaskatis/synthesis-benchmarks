//Andreas : Relaxed version of black box fuzzer to enable the generation of invalid inputs
#include "ptaas.h"
#include <assert.h>
#include <time.h>
static int init = 0;
int emission_b[1];
int emission_g[1];
int aeval_tmp_rand_int_12[1];
int emission_r[1];
int aeval_tmp_rand_int_11[1];
int color_b[1];
int color_r[1];
int aeval_tmp_rand_int_8[1];
int aeval_tmp_rand_int_13[1];
int vector_z[1];
int vector_y[1];
int color_g[1];
int aeval_tmp_rand_int_6[1];
int vector_x[1];
int aeval_tmp_rand_int_5[1];
int position_y[1];
int aeval_tmp_rand_int_7[1];
int position_x[1];
int aeval_tmp_rand_int_3[1];
int aeval_tmp_rand_int_10[1];
int position_z[1];
int aeval_tmp_rand_int_1[1];
int aeval_tmp_rand_int_0[1];
int aeval_tmp_rand_int_2[1];
int aeval_tmp_rand_int_4[1];
int object[1];
int aeval_tmp_rand_int_9[1];
int aeval_tmp_rand_int_14[1];
int spec[1];
int parm[1];
void skolem_0() {

  aeval_tmp_rand_int_0[0] = generateRandomValue(1, 1, 0, 5);
  //assert((0 <= (aeval_tmp_rand_int_0[0])) && ((aeval_tmp_rand_int_0[0]) <= 5));

  object[0] = aeval_tmp_rand_int_0[0];
  aeval_tmp_rand_int_1[0] = generateRandomValue(1, 1, 0, 2);
  //assert((0 <= (aeval_tmp_rand_int_1[0])) && ((aeval_tmp_rand_int_1[0]) <= 1));

  spec[0] = aeval_tmp_rand_int_1[0];
  aeval_tmp_rand_int_2[0] = generateRandomValue(1, 1, -1023, 1023);
  //assert((0 <= (aeval_tmp_rand_int_2[0])) && ((aeval_tmp_rand_int_2[0]) <= 1023));

  parm[0] = aeval_tmp_rand_int_2[0];
  aeval_tmp_rand_int_3[0] = generateRandomValue(1, 1, (-1024), 1024);
  //assert((((-1024)) <= (aeval_tmp_rand_int_3[0])) && ((aeval_tmp_rand_int_3[0]) <= 1024));

  position_x[0] = aeval_tmp_rand_int_3[0];
  aeval_tmp_rand_int_4[0] = generateRandomValue(1, 1, (-1024), 1024);
  //assert((((-1024)) <= (aeval_tmp_rand_int_4[0])) && ((aeval_tmp_rand_int_4[0]) <= 1024));

  position_y[0] = aeval_tmp_rand_int_4[0];
  aeval_tmp_rand_int_5[0] = generateRandomValue(1, 1, (-1024), 1024);
  //assert((((-1024)) <= (aeval_tmp_rand_int_5[0])) && ((aeval_tmp_rand_int_5[0]) <= 1024));

  position_z[0] = aeval_tmp_rand_int_5[0];
  aeval_tmp_rand_int_6[0] = generateRandomValue(1, 1, (-1024), 1024);
  //assert((((-1024)) <= (aeval_tmp_rand_int_6[0])) && ((aeval_tmp_rand_int_6[0]) <= 1024));

  vector_x[0] = aeval_tmp_rand_int_6[0];
  aeval_tmp_rand_int_7[0] = generateRandomValue(1, 1, (-1024), 1024);
  //assert((((-1024)) <= (aeval_tmp_rand_int_7[0])) && ((aeval_tmp_rand_int_7[0]) <= 1024));

  vector_y[0] = aeval_tmp_rand_int_7[0];
  aeval_tmp_rand_int_8[0] = generateRandomValue(1, 1, (-1024), 1024);
  //assert((((-1024)) <= (aeval_tmp_rand_int_8[0])) && ((aeval_tmp_rand_int_8[0]) <= 1024));

  vector_z[0] = aeval_tmp_rand_int_8[0];
  aeval_tmp_rand_int_9[0] = generateRandomValue(1, 1, -1024, 1024);
  //assert((0 <= (aeval_tmp_rand_int_9[0])) && ((aeval_tmp_rand_int_9[0]) <= 1023));

  color_r[0] = aeval_tmp_rand_int_9[0];
  aeval_tmp_rand_int_10[0] = generateRandomValue(1, 1, -1024, 1024);
  //assert((0 <= (aeval_tmp_rand_int_10[0])) && ((aeval_tmp_rand_int_10[0]) <= 1023));

  color_g[0] = aeval_tmp_rand_int_10[0];
  aeval_tmp_rand_int_11[0] = generateRandomValue(1, 1, -1024, 1024);
  //assert((0 <= (aeval_tmp_rand_int_11[0])) && ((aeval_tmp_rand_int_11[0]) <= 1023));

  color_b[0] = aeval_tmp_rand_int_11[0];
  aeval_tmp_rand_int_12[0] = generateRandomValue(1, 1, -1024, 1024);
  //assert((0 <= (aeval_tmp_rand_int_12[0])) && ((aeval_tmp_rand_int_12[0]) <= 1023));

  emission_r[0] = aeval_tmp_rand_int_12[0];
  aeval_tmp_rand_int_13[0] = generateRandomValue(1, 1, -1024, 1024);
  //assert((0 <= (aeval_tmp_rand_int_13[0])) && ((aeval_tmp_rand_int_13[0]) <= 1023));

  emission_g[0] = aeval_tmp_rand_int_13[0];
  aeval_tmp_rand_int_14[0] = generateRandomValue(1, 1, -1024, 1024);
  //assert((0 <= (aeval_tmp_rand_int_14[0])) && ((aeval_tmp_rand_int_14[0]) <= 1023));

  emission_b[0] = aeval_tmp_rand_int_14[0];
  return;
}


void updateFunction() {
  srand(time(NULL));

if (init == 0) {
  skolem_0();
  init = init + 1;
} else {
  skolem_0();
}
return;
}


