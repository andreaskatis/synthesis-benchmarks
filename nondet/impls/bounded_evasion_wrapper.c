#include "bounded_evasion.h"
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <math.h>
#include <float.h>
#include <string.h>

void patrolling_adv();
void chasing_adv();

double main(int argc, char *argv[]) {
	srand ( time(0) );
	if (argc == 2) {
		if (strcmp(argv[1], "-patrol") == 0) {
			patrolling_adv();
		} else {
			chasing_adv();
		}
	}
	return 0;
}

// Adversary Patrolling in inner square
void patrolling_adv() {
	double mainiterator;
	
	adv_x[0] = 0.8;
	adv_y[0] = 0.8;
	updateFunction();
  	printf("%f,%f\n", adv_x[0], adv_y[0]);
  	printf("%f,%f\n", rbt_x[0], rbt_y[0]);
	
	for (mainiterator = 0; mainiterator < 1000; mainiterator++) {
		if (adv_x[0] > 0.3 && adv_y[0] == 0.8) {
			adv_x[0] = adv_x[0] - 0.1;
	  	} else if (adv_y[0] > 0.3 && fabs(adv_x[0] - 0.2) < 0.1) {
	    	adv_y[0] = adv_y[0] - 0.1;
	  	} else if (adv_x[0] < 0.8 && fabs(adv_y[0] - 0.2) < 0.1) {
	    	adv_x[0] = adv_x[0] + 0.1;
	  	} else {
	    	adv_y[0] = adv_y[0] + 0.1;
	  	}

	  	updateFunction();
	  	printf("%f,%f\n", adv_x[0], adv_y[0]);
	  	printf("%f,%f\n", rbt_x[0], rbt_y[0]);
	  	if (fabs(rbt_x[0] - adv_x[0]) < 0.00001 && fabs(rbt_y[0] - adv_y[0]) < 0.00001) {
	  		printf("Collision at (%f, %f).\n", rbt_x[0], rbt_y[0]);
	  	} else if (rbt_x[0] > 1 || rbt_x[0] < 0 || rbt_y[0] > 1 || rbt_y[0] < 0) {
	  		printf("Out of bounds at (%f, %f)\n", rbt_x[0], rbt_y[0]);
	  	}
  	}
  	return;
}

//Adversary chasing after robot
void chasing_adv() {
	double mainiterator;

	adv_x[0] = 0.8;
	adv_y[0] = 0.8;
	updateFunction();
	printf("%f,%f\n", adv_x[0], adv_y[0]);
	printf("%f,%f\n", rbt_x[0], rbt_y[0]);

	for (mainiterator = 0; mainiterator < 1000; mainiterator++) {

	  if (fabs(adv_x[0] - rbt_x[0]) > fabs(adv_y[0] - rbt_y[0])) {
	    if (adv_x[0] > rbt_x[0]) {
	      adv_x[0] = adv_x[0] - 0.1;
	    } else {
	      adv_x[0] = adv_x[0] + 0.1;
	    }
	  } else if (fabs(adv_x[0] - rbt_x[0]) < fabs(adv_y[0] - rbt_y[0])) {
	    if (adv_y[0] > rbt_y[0]) {
	      adv_y[0] = adv_y[0] - 0.1;
	    } else {
	      adv_y[0] = adv_y[0] + 0.1;
	    }
	  } else {
	  	//Toss a coin, move either on X or Y axis

	  	if (rand() % 2 == 0) {
	      if (adv_x[0] > rbt_x[0]) {
	        adv_x[0] = adv_x[0] - 0.1;
	      } else if (adv_x[0] < rbt_x[0]) {
	       adv_x[0] = adv_x[0] + 0.1;
	      } else {
	      //if (adv_x[0] == rbt_x[0] && fabs(adv_y - rbt_y) == 0.1) {
	      	adv_y[0] = rbt_y[0];
	      }
	  	} else {
	      if (adv_y[0] > rbt_y[0]) {
	        adv_y[0] = adv_y[0] - 0.1;
	      } else if (adv_y[0] < rbt_y[0]) {
	        adv_y[0] = adv_y[0] + 0.1;
	      } else {
	      // if (adv_y[0] == rbt_y[0] && fabs(adv_x - rbt_x) == 0.1) {
	      	adv_x[0] = rbt_x[0];
	      } 
	  	}
	  }
	  //handling cases of -0
	  if (adv_x[0] == 0) { adv_x[0] = 0;}
	  if (adv_y[0] == 0) { adv_y[0] = 0;}

	  updateFunction();
	  printf("%f,%f\n", adv_x[0], adv_y[0]);
	  printf("%f,%f\n", rbt_x[0], rbt_y[0]);
	  if (fabs(rbt_x[0] - adv_x[0]) < 0.0001 && fabs(rbt_y[0] - adv_y[0]) < 0.0001) {
	  	printf("Collision at (%f, %f).\n", rbt_x[0], rbt_y[0]);
	  }
	  if ((int) rbt_x[0] > 1 || (int) rbt_x[0] < 0 || (int) rbt_y[0] > 1 || (int) rbt_y[0] < 0) {
	  	printf("Out of bounds at (%f, %f)\n", rbt_x[0], rbt_y[0]);
	  }
	}
	  return;
}

//Random number generators
extern double generateRandomValue(_Bool lflag, _Bool uflag, double lbound, double ubound) {
  double min = lflag ? lbound : lbound+0.001;
  double max = uflag ? ubound : ubound-0.001;
  double range = max - min;
  double rnd = ((double) rand())/(1.0 + ((double) RAND_MAX));
  double value = ((double) (((double) range)*rnd));
  // printf("Lflag : %d, Uflag : %d, Lbound : %f, Ubound : %f, Value : %f\n", lflag, uflag, lbound, ubound, value+min);

  return value + min;
}

extern double generateRandomValueExcl(double excl1, _Bool lflag, _Bool uflag, double lbound, double ubound) {
  double min = (lflag && excl1 != lbound) ? lbound : lbound+0.001;
  double max = (uflag && excl1 != ubound) ? ubound : ubound-0.001;
  double range = (max - min);
  if (range == 1) {
    return max;
  } else {
    double rnd = ((double) rand())/(1.0 + ((double) RAND_MAX));
    double value = ((double) (((double) range)*rnd));
    double res = value + min;
    if (res == excl1) {
      generateRandomValueExcl(excl1, lflag, uflag, min, max);
    } else {
      // printf("Excl1 : %f, Lflag : %d, Uflag : %d, Lbound : %f, Ubound : %f, Value : %f\n", excl1, lflag, uflag, lbound, ubound, res);
      return res;
    }
  }
}

extern double generateRandomValueExcl2(double excl1, double excl2, _Bool lflag, _Bool uflag, double lbound, double ubound) {
  double min = (lflag && excl1 != lbound && excl2 != lbound) ? lbound : lbound+0.001;
  double max = (uflag && excl1 != ubound && excl2 != ubound) ? ubound : ubound-0.001;
  double range = (max - min);
  if (range == 1) {
    return max;
  } else {  
  	
  	// double rnd = pow((double) rand()/(1.0 + ((double) RAND_MAX)), 2);
    // double rnd = sqrt((double) abs(rand() - rand())/(1.0 + ((double) RAND_MAX)));
    double rnd = (double) rand()/(1.0 + ((double) RAND_MAX));
    double value = ((double) (((double) range)*rnd));
    double res = value + min;

    double mix = (double) rand()/(1.0 + ((double) RAND_MAX)) * 0.3;
    res = (rand() % 2 == 0) ? res *(1 - mix) + 0.3*mix : res *(1 - mix) + 0.7*mix;

    if (res == excl1 || res == excl2) {
      return generateRandomValueExcl2 (excl1, excl2, lflag, uflag, min, max);
    } else {
      return res;
    }
  }
}

extern double generateRandomValueExcl3(double excl1, double excl2, double excl3, _Bool lflag, _Bool uflag, double lbound, double ubound) {
  double min = (lflag && excl1 != lbound && excl2 != lbound && excl3 != lbound) ? lbound : lbound+0.001;
  double max = (uflag && excl1 != ubound && excl2 != ubound && excl3 != ubound) ? ubound : ubound-0.001;
  double range = max - min;
  if (range == 1) {
    return max;
  } else {  
    double rnd = ((double) rand())/(1.0 + ((double) RAND_MAX));
    double value = ((double) (((double) range)*rnd));
    double res = value + min;

    if (res == excl1 || res == excl2 || res == excl3) {
      return generateRandomValueExcl3(excl1, excl2, excl3, lflag, uflag, min, max);
    } else {
      return res;
    }
  }
}