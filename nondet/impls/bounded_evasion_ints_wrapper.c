#include "bounded_evasion_ints.h"
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <math.h>
#include <string.h>
void patrolling_adv();
void chasing_adv();

int main(int argc, char *argv[]) {
	srand ( time(NULL) );
	if (argc == 2) {
		if (strcmp(argv[1], "-patrol") == 0) {
			patrolling_adv();
		} else {
			chasing_adv();
		}
	}
	return 0;
}

void patrolling_adv() {
	int mainiterator;
	adv_x[0] = 5;
	adv_y[0] = 5;
	updateFunction();
	printf("%d,%d\n", adv_x[0], adv_y[0]);
	printf("%d,%d\n", rbt_x[0], rbt_y[0]);
	
	for (mainiterator = 0; mainiterator < 1000; mainiterator++) {
		if (adv_x[0] > 1 && adv_y[0] == 5) {
			adv_x[0] = adv_x[0] - 1;
	  	} else if (adv_y[0] > 1 && (adv_x[0] == 1)) {
	    	adv_y[0] = adv_y[0] - 1;
	  	} else if (adv_x[0] < 5 && (adv_y[0] == 1)) {
	    	adv_x[0] = adv_x[0] + 1;
	  	} else {
	    	adv_y[0] = adv_y[0] + 1;
	  	}

	  	updateFunction();
	  	printf("%d,%d\n", adv_x[0], adv_y[0]);
	  	printf("%d,%d\n", rbt_x[0], rbt_y[0]);
	  	if(adv_x[0] == rbt_x[0] && adv_y[0] == rbt_y[0]) {
	  		printf("Collision at (%d, %d).\n", rbt_x[0], rbt_y[0]);
	  	} else if (rbt_x[0] > 6 || rbt_x[0] < 0 || rbt_y[0] > 6 || rbt_y[0] < 0) {
    		printf("Out of bounds at (%d, %d)\n", rbt_x[0], rbt_y[0]);
    	}
  	}
	return;
}
void chasing_adv() {
	int mainiterator;
	adv_x[0] = 6;
	adv_y[0] = 6;
	updateFunction();
	printf("%d,%d\n", adv_x[0], adv_y[0]);
	printf("%d,%d\n", rbt_x[0], rbt_y[0]);
	for (mainiterator = 0; mainiterator < 1000; mainiterator++) {
	  if (abs(adv_x[0] - rbt_x[0]) > abs(adv_y[0] - rbt_y[0])) {
	    if (adv_x[0] > rbt_x[0]) {
	      adv_x[0] = adv_x[0] - 1;
	    } else {
	      adv_x[0] = adv_x[0] + 1;
	    }
	  } else if (abs(adv_x[0] - rbt_x[0]) < abs(adv_y[0] - rbt_y[0])) {
	    if (adv_y[0] > rbt_y[0]) {
	      adv_y[0] = adv_y[0] - 1;
	    } else {
	      adv_y[0] = adv_y[0] + 1;
	    }
	  } else {
	    // Flip a coin: Move either along X or Y axis
	    if (rand() % 2 == 0) {
	      if (adv_x[0] > rbt_x[0]) {
	        adv_x[0] = adv_x[0] - 1;
	      } else {
	       adv_x[0] = adv_x[0] + 1;
	      }
	    } else {
	      if (adv_y[0] > rbt_y[0]) {
	        adv_y[0] = adv_y[0] - 1;
	      } else {
	        adv_y[0] = adv_y[0] + 1;
	      } 
	    }
	  }
	  updateFunction();
	  printf("%d,%d\n", adv_x[0], adv_y[0]);
	  printf("%d,%d\n", rbt_x[0], rbt_y[0]);
	  if(adv_x[0] == rbt_x[0] && adv_y[0] == rbt_y[0]) {
	  	printf("Collision at (%d, %d).\n", rbt_x[0], rbt_y[0]);
	  } else if (rbt_x[0] > 6 || rbt_x[0] < 0 || rbt_y[0] > 6 || rbt_y[0] < 0) {
	    printf("Out of bounds at (%d, %d)\n", rbt_x[0], rbt_y[0]);
	  }
	}
	return;
}


extern int generateRandomValue(_Bool lflag, _Bool uflag, int lbound, int ubound) {
  int min = lflag ? lbound : lbound+1;
  int max = uflag ? ubound : ubound-1;
  int range = max - min + 1;
  double rnd = ((double) rand())/(1.0 + ((double) RAND_MAX));
  int value = ((int) (((double) range)*rnd));
  return value + min;
}

extern int generateRandomValueExcl(int excl1, _Bool lflag, _Bool uflag, int lbound, int ubound) {
  int min = (lflag && excl1 != lbound) ? lbound : lbound+1;
  int max = (uflag && excl1 != ubound) ? ubound : ubound-1;
  int range = max - min + 1;
  if (range == 1) {
    return max;
  } else {
    double rnd = ((double) rand())/(1.0 + ((double) RAND_MAX));
    int value = ((int) (((double) range)*rnd));
    int res = value + min;
    if (res == excl1) {
      generateRandomValueExcl(excl1, 1, 1, min, max);
    } else {
      return res;
    }
  }
}

extern int generateRandomValueExcl2(int excl1, int excl2, _Bool lflag, _Bool uflag, int lbound, int ubound) {
  int min = (lflag && excl1 != lbound && excl2 != lbound) ? lbound : lbound+1;
  int max = (uflag && excl1 != ubound && excl2 != ubound) ? ubound : ubound-1;
  int range = max - min + 1;
  if (range == 1) {
    return max;
  } else {  
    double rnd = ((double) rand())/(1.0 + ((double) RAND_MAX));
    int value = ((int) (((double) range)*rnd));
    int res = value + min;
    if (res == excl1 || res == excl2) {
      return generateRandomValueExcl2 (excl1, excl2, 1, 1, min, max);
    } else {
      return res;
    }
  }
}

extern int generateRandomValueExcl3(int excl1, int excl2, int excl3, _Bool lflag, _Bool uflag, int lbound, int ubound) {
  int min = (lflag && excl1 != lbound && excl2 != lbound && excl3 != lbound) ? lbound : lbound+1;
  int max = (uflag && excl1 != ubound && excl2 != ubound && excl3 != ubound) ? ubound : ubound-1;
  int range = max - min + 1;
  if (range == 1) {
    return max;
  } else {  
    double rnd = ((double) rand())/(1.0 + ((double) RAND_MAX));
    int value = ((int) (((double) range)*rnd));
    int res = value + min;
    if (res == excl1 || res == excl2 || res == excl3) {
      return generateRandomValueExcl3(excl1, excl2, excl3, 1, 1, min, max);
    } else {
      return res;
    }
  }
}