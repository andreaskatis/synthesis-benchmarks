#include "ptaas.h"
#include <assert.h>

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
  aeval_tmp_rand_int_0[0] = generateRandomValue(1, 1, 0, 4);
  //assert((0 <= (aeval_tmp_rand_int_0[0])) && ((aeval_tmp_rand_int_0[0]) <= 5));

  object[0] = aeval_tmp_rand_int_0[0];
  aeval_tmp_rand_int_1[0] = generateRandomValue(1, 1, 0, 1);
  //assert((0 <= (aeval_tmp_rand_int_1[0])) && ((aeval_tmp_rand_int_1[0]) <= 1));

  spec[0] = aeval_tmp_rand_int_1[0];
  aeval_tmp_rand_int_2[0] = generateRandomValue(1, 1, 0, 255);
  //assert((0 <= (aeval_tmp_rand_int_2[0])) && ((aeval_tmp_rand_int_2[0]) <= 255));

  parm[0] = aeval_tmp_rand_int_2[0];
  aeval_tmp_rand_int_3[0] = generateRandomValue(1, 1, (-256), 256);
  //assert((((-256)) <= (aeval_tmp_rand_int_3[0])) && ((aeval_tmp_rand_int_3[0]) <= 256));

  position_x[0] = aeval_tmp_rand_int_3[0];
  aeval_tmp_rand_int_4[0] = generateRandomValue(1, 1, (-256), 256);
  //assert((((-256)) <= (aeval_tmp_rand_int_4[0])) && ((aeval_tmp_rand_int_4[0]) <= 256));

  position_y[0] = aeval_tmp_rand_int_4[0];
  aeval_tmp_rand_int_5[0] = generateRandomValue(1, 1, (-256), 256);
  //assert((((-256)) <= (aeval_tmp_rand_int_5[0])) && ((aeval_tmp_rand_int_5[0]) <= 256));

  position_z[0] = aeval_tmp_rand_int_5[0];
  aeval_tmp_rand_int_6[0] = generateRandomValue(1, 1, (-256), 256);
  //assert((((-256)) <= (aeval_tmp_rand_int_6[0])) && ((aeval_tmp_rand_int_6[0]) <= 256));

  vector_x[0] = aeval_tmp_rand_int_6[0];
  aeval_tmp_rand_int_7[0] = generateRandomValue(1, 1, (-256), 256);
  //assert((((-256)) <= (aeval_tmp_rand_int_7[0])) && ((aeval_tmp_rand_int_7[0]) <= 256));

  vector_y[0] = aeval_tmp_rand_int_7[0];
  aeval_tmp_rand_int_8[0] = generateRandomValue(1, 1, (-256), 256);
  //assert((((-256)) <= (aeval_tmp_rand_int_8[0])) && ((aeval_tmp_rand_int_8[0]) <= 256));

  vector_z[0] = aeval_tmp_rand_int_8[0];
  aeval_tmp_rand_int_9[0] = generateRandomValue(1, 1, (-256), 256);
  //assert((0 <= (aeval_tmp_rand_int_9[0])) && ((aeval_tmp_rand_int_9[0]) <= 255));

  color_r[0] = aeval_tmp_rand_int_9[0];
  aeval_tmp_rand_int_10[0] = generateRandomValue(1, 1, 0, 256);
  //assert((0 <= (aeval_tmp_rand_int_10[0])) && ((aeval_tmp_rand_int_10[0]) <= 255));

  color_g[0] = aeval_tmp_rand_int_10[0];
  aeval_tmp_rand_int_11[0] = generateRandomValue(1, 1, 0, 256);
  //assert((0 <= (aeval_tmp_rand_int_11[0])) && ((aeval_tmp_rand_int_11[0]) <= 255));

  color_b[0] = aeval_tmp_rand_int_11[0];
  aeval_tmp_rand_int_12[0] = generateRandomValue(1, 1, 0, 256);
  //assert((0 <= (aeval_tmp_rand_int_12[0])) && ((aeval_tmp_rand_int_12[0]) <= 255));

  emission_r[0] = aeval_tmp_rand_int_12[0];
  aeval_tmp_rand_int_13[0] = generateRandomValue(1, 1, 0, 256);
  //assert((0 <= (aeval_tmp_rand_int_13[0])) && ((aeval_tmp_rand_int_13[0]) <= 255));

  emission_g[0] = aeval_tmp_rand_int_13[0];
  aeval_tmp_rand_int_14[0] = generateRandomValue(1, 1, 0, 256);
  //assert((0 <= (aeval_tmp_rand_int_14[0])) && ((aeval_tmp_rand_int_14[0]) <= 255));

  emission_b[0] = aeval_tmp_rand_int_14[0];
  return;
}


void updateFunction() {
if (init == 0) {
  skolem_0();
  init = init + 1;
} else {
  skolem_0();
}
return;
}


