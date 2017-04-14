import os, subprocess, sys, glob, shutil
import numpy as np
import matplotlib.pyplot as plt
#
# Configuration
#

EXPERIMENTS_DIR = 'verification'
PUSH_PATH = 'kind'
ANOTHER_PUSH_PATH = 'fixpoint'
IMPLEMENT_DIR = 'verification/kind'
ANOTHER_IMPLEMENT_DIR = "verification/fixpoint"


SECOND_EXPERIMENTS_DIR = 'smaccm'
SECOND_IMPLEMENT_DIR = 'smaccm/kind'
SECOND_ANOTHER_IMPLEMENT_DIR = 'smaccm/fixpoint'

EXTRA_EXPERIMENTS_DIR = "fixpoint_only"
EXTRA_IMPLEMENT_DIR = 'fixpoint_only/kind'
EXTRA_ANOTHER_IMPLEMENT_DIR = 'fixpoint_only/fixpoint'



NestList_overhead = []
NestList_size = [] 
NestList_size_name = []
NestList_size_name_verification = []
NestList_size_name_smaccm = []
NestList_performance = []
#TIMEOUT = 3600


#
# Run JKind
#
# '-timeout', str(TIMEOUT)
#file_path = verification/car_1.lus

def run_realizability(file_path):
    #delete "xml"
    args = ['java', '-jar', jkind_jar, '-jrealizability',
            '-timeout', '1000', '-n', '1000000', file_path]
    with open("debug_jkind.txt", "a") as debug:
        debug.write("Running jkind with arguments: {}\n".format(args))
        proc = subprocess.Popen(args, stdout=debug)
        proc.wait()
        debug.write("\n")

def run_synthesis(file_path):
    args = ['java', '-jar', jkind_jar, '-jrealizability',
            '-synthesis', '-timeout', '1000', '-n', '1000000', file_path]
    with open("debug_jkind.txt", "a") as debug:
        debug.write("Running jkind with arguments: {}\n".format(args))
        proc = subprocess.Popen(args, stdout=debug)
        proc.wait()
        debug.write("\n")

def run_fixpoint(file_path):
    args = ['java', '-jar', jkind_jar, '-jrealizability',
            '-fixpoint', '-timeout', '1000', '-n', '1000000', file_path]
    with open("debug_jkind.txt", "a") as debug:
        debug.write("Running jkind with arguments: {}\n".format(args))
        proc = subprocess.Popen(args, stdout=debug)
        proc.wait()
        debug.write("\n")


def run_realizability_synthesis(lus_file, experiments_dir): 

    lus_path = os.path.join(experiments_dir, lus_file)
    run_realizability(lus_path)
    sys.stdout.write(".")
    sys.stdout.flush()

    lus_path = os.path.join(experiments_dir, lus_file)
    run_synthesis(lus_path)
    sys.stdout.write(".")
    sys.stdout.flush()

def run_last_fixpoint(lus_file, experiments_dir):  
    lus_path = os.path.join(experiments_dir, lus_file)
    run_fixpoint(lus_path)
    sys.stdout.write(".")
    sys.stdout.flush()



def move_impl(outpath, experiments_dir): 
    impl_files = glob.glob("*_skolem.smt2")
    if len(impl_files) == 0:
        print("No implement files found in '" + experiments_dir + "' directory")
        sys.exit(-1)
    #print("moving impl files")
    for i, impl_file in enumerate(impl_files):
        old_implPath = impl_file
        new_implPath = os.path.join(outpath, impl_file)
        shutil.move(old_implPath, new_implPath)

    #remove dummy smt2files
    smt_files = glob.glob("*.smt2")
    if (len(smt_files)!=0):
        for i, smt_file in enumerate(smt_files):
            os.remove(smt_file)







# '-timeout', str(TIMEOUT)

def run_smtlib2c(impl_file, implement_dir): 
    file_path = os.path.join(implement_dir, impl_file)
    args = ['java', '-jar', smtlib2c_jar,
            '-iter', '1000000',
            '-c_harness', '-lustrec_harness', '-lustrecnode', 'top', file_path]
    with open(implement_dir+"/debug_smtlib2c.txt", "a") as debug:
        debug.write("Running SMTLib2C with arguments: {}\n".format(args))
        proc = subprocess.Popen(args, stdout=debug)
        proc.wait()
        debug.write("\n")


def run_makefile(file_path):
    args = ['make', 'FILE='+file_path]
    with open("debug_make.txt", "a") as debug:
        debug.write("Running make for file: {}\n".format(args))
        proc = subprocess.Popen(args, stdout=debug)
        proc.wait()
        debug.write("\n")


def run_executables(file_path):
    args = ['./'+file_path]
    with open("results.txt", "a") as debug:
        proc = subprocess.Popen(args, stdout=debug)
        proc.wait()



def parse(target, output):
    with open(target,'r') as f:
        with open(output, 'a') as op:
            for line in f:
                if ("REALIZABLE" in line):
                    op.write(line)

    op.close()
    f.close()


def writeOverhead(nestList, tempOverhead):
    with open(tempOverhead,'r') as f:
        count = 0
        index = 0
        for line in f:
            lst = line.split(" ")
            time = lst[-1].replace("s","").strip()
            nestList[index].append(time)
            count = count + 1
            if (count==3):
                index = index+1
                count = 0
            
    f.close()


def drawOverhead():
    font = {'family' : 'normal','weight' : 'bold', 'size' : 20}
    plt.rc('font', **font)
    # pl1 = np.array([float(j[1]) for j in sorted(NestList_overhead, key=lambda res: res[1])])
    # pl2 = np.array([float(j[2]) for j in sorted(NestList_overhead, key=lambda res: res[1])])
    # pl3 = np.array([float(j[3]) for j in sorted(NestList_overhead, key=lambda res: res[1])])

    pl1 = np.array([float(j[1]) for j in NestList_overhead])
    pl2 = np.array([float(j[2]) for j in NestList_overhead])
    pl3 = np.array([float(j[3]) for j in NestList_overhead])


    #print(sorted(NestList_overhead, key=lambda res: res[1]))

    fig = plt.figure()

    plt.yscale('log')
    
    realizability = plt.plot(pl1,'-bs', label = 'JRealizability')
    synthesis = plt.plot(pl2,'-r^', label = 'Synthesis')
    fixpoint = plt.plot(pl3,'-g^', label = 'Fixpoint')

    plt.xlabel("Model")
    plt.ylabel("Performance (seconds)")

    plt.legend(bbox_to_anchor=(0.6, 1))

    fig.savefig("overhead.pdf")



def measureSizeOfC(path, NestList_size_name_var):
    os.chdir(path)
    for cname in NestList_size_name_var:
        os.system('wc -l ' + cname[0] + ' |grep -v total >> loc.txt' )
    os.chdir("..")
    os.chdir("..")


def drawSize():
    font = {'family' : 'normal', 'weight' : 'bold', 'size' : 20}
    plt.rc('font', **font)

    #pl2 = [j[1] for j in (sorted(NestList_size, key=lambda x: x[1]))]
    #pl4 = [j[2] for j in (sorted(NestList_size, key=lambda x: x[1]))]

    pl1 = np.array([j[1] for j in NestList_size])
    pl2 = np.array([j[2] for j in NestList_size])

#(pl1,pl2) = zip(*pl3)

# Plot the results
    fig = plt.figure()
    plt.yscale('log')
    
    synthesized = plt.plot(pl1,'-r^', label = 'synthesized')
    fixpoint = plt.plot(pl2,'-bs', label = 'fixpoint')
#handwritten = plt.plot(pl1,'-bs', label = 'handwritten')

    plt.xlabel("Model")
    plt.ylabel("Lines of Code")
    plt.legend(loc = 'upper left')
    fig.savefig("loc.pdf")



def combineSizeTxt(file1, file2):
    with open(file1, "r") as f1:
        count= 0 
        for line1 in f1:
            tempList1 = []
            lst = line1.strip().split(" ")

            tempList1.append(lst[1])
            tempList1.append(lst[0])

            with open(file2, "r") as f2:
                for line2 in f2:
                    tempList2 = line2.strip().split(" ")
                    if (tempList2[1] == tempList1[0]):
                        tempList1.append(tempList2[0])

            NestList_size.append(tempList1)
            

    f1.close()
    f2.close()

#same folder
def combineResultTxt(file1, file2):
    with open(file1, "r") as f1:
        count= 0 
        for line1 in f1:
            tempList1 = []
            lst = line1.strip().split(" ")

            tempList1.append(lst[0])
            tempList1.append(lst[1])

            with open(file2, "r") as f2:
                for line2 in f2:
                    tempList2 = line2.strip().split(" ")
                
                    if (tempList2[0] == tempList1[0]):
                        tempList1.append(tempList2[1])

            NestList_performance.append(tempList1)
            

    f1.close()
    f2.close()


def drawPerformance():
    font = {'family' : 'normal','weight' : 'bold','size' : 20}
    plt.rc('font', **font)


#    pl1 = np.array([float(j[1]) for j in (sorted(NestList_performance, key=lambda x: x[1]))])
#    pl2 = np.array([float(j[2]) for j in (sorted(NestList_performance, key=lambda x: x[1]))])
    
    pl1 = np.array([float(j[1]) for j in NestList_performance])
    pl2 = np.array([float(j[2]) for j in NestList_performance])

    fig = plt.figure()
    plt.yscale('log')
    
    synthesized = plt.plot(pl1,'-r^', label = 'synthesized')
    fixpoint = plt.plot(pl2,'-bs', label = 'fixpoint')
#handwritten = plt.plot(pl1,'-bs', label = 'handwritten')

    plt.xlabel("Model")
    plt.ylabel("Performance")
    plt.legend(loc = 'upper left')
    fig.savefig("performance.pdf")





################################################################################################
################################################################################################
################################################################################################

# Gather Lustre files

def execute(experiments_dir, push_path, another_push_path, implement_dir, another_implement_dir, NestList_size_name_var):
    if not os.path.exists(experiments_dir):
        print("'" + experiments_dir + "' directory does not exist")
        sys.exit(-1)
    os.chdir(experiments_dir)
    lus_files = glob.glob("*.lus")
    if len(lus_files) == 0:
        print("No Lustre files found in '" + experiments_dir + "' directory")
        sys.exit(-1)
    os.chdir("..")

#
# Find jkind.jar
#

#exeute...................................................
    with open("lustreName.txt", "a") as file:
        if ((len(sys.argv)>1) and (sys.argv[1] == "-skipjkind")):
            print("skip the jkind")
            for i, lus_file in enumerate(lus_files):
                empty = []
                empty.append(lus_file)
                NestList_overhead.append(empty)


        else:
            for i, lus_file in enumerate(lus_files):
                empty = []
                empty.append(lus_file)
                NestList_overhead.append(empty)  # set the name of file 

                file.write(lus_file+"\n")

                sys.stdout.write("({} of {}) {} [".format(i+1, len(lus_files), lus_file))
                sys.stdout.flush()

                run_realizability_synthesis(lus_file, experiments_dir)
                os.chdir(experiments_dir)
                move_impl(push_path, experiments_dir)
                os.chdir("..")
    
                run_last_fixpoint(lus_file, experiments_dir)
                os.chdir(experiments_dir)
                move_impl(another_push_path, experiments_dir)
                os.chdir("..")


                sys.stdout.write("]\n")
                sys.stdout.flush()


    file.close()
    #print(NestList_overhead)


#do the run_smtlib2c.................................................

    print("Running run_smtlib2c")



#execute run_smtlib2c in kind

    if not os.path.exists(implement_dir):
        print("'" + implement_dir + "' directory does not exist")
        sys.exit(-1)
    os.chdir(implement_dir)
    impl_files = glob.glob("*_skolem.smt2")
    if len(impl_files) == 0:
        print("No Skolem files found in '" + implement_dir + "' directory")
        sys.exit(-1)
    os.chdir("..")
    os.chdir("..")

    


    for i, impl_file in enumerate(impl_files):
        sys.stdout.write("({} of {}) {} [".format(i+1, len(impl_files), impl_file))
        sys.stdout.flush()
        run_smtlib2c(impl_file, implement_dir)
        sys.stdout.write(".")
        sys.stdout.flush()
        sys.stdout.write("]\n")
        sys.stdout.flush()


#execute run_smtlib2c in fixpoint

    if not os.path.exists(another_implement_dir):
        print("'" + another_implement_dir + "' directory does not exist")
        sys.exit(-1)
    os.chdir(another_implement_dir)
    impl_files = glob.glob("*_skolem.smt2")
    if len(impl_files) == 0:
        print("No Skolem files found in '" + another_implement_dir + "' directory")
        sys.exit(-1)
    os.chdir("..")
    os.chdir("..")

    


    for i, impl_file in enumerate(impl_files):
        sys.stdout.write("({} of {}) {} [".format(i+1, len(impl_files), impl_file))
        sys.stdout.flush()
        run_smtlib2c(impl_file, another_implement_dir)
        sys.stdout.write(".")
        sys.stdout.flush()
        sys.stdout.write("]\n")
        sys.stdout.flush()



    print("Running run_make")

    if not os.path.exists(experiments_dir):
        print("'" + experiments_dir + "' directory does not exist")
        sys.exit(-1)
    os.chdir(experiments_dir)
    lus_files = glob.glob("*.lus")
    if len(lus_files) == 0:
        print("No Lustre files found in '" + experiments_dir + "' directory")
        sys.exit(-1)
    os.chdir("..")



#execute run_make in kind..................................

    os.chdir(implement_dir)
    for i, lus_file in enumerate(lus_files):
        sys.stdout.write("({} of {}) {} [".format(i+1, len(lus_files), lus_file))
        sys.stdout.flush()
        run_makefile(os.path.splitext(lus_file)[0])
        sys.stdout.write(".")
        sys.stdout.flush()
        sys.stdout.write("]\n")
        sys.stdout.flush()


#execute run_make in fixpoint..................................
    os.chdir("..")
    os.chdir("..")

    os.chdir(another_implement_dir)
    for i, lus_file in enumerate(lus_files):
        sys.stdout.write("({} of {}) {} [".format(i+1, len(lus_files), lus_file))
        sys.stdout.flush()
        run_makefile(os.path.splitext(lus_file)[0])
        sys.stdout.write(".")
        sys.stdout.flush()
        sys.stdout.write("]\n")
        sys.stdout.flush()




    print("Running the run_executable")
    os.chdir("..")
    os.chdir("..")




    if not os.path.exists(experiments_dir):
        print("'" + experiments_dir + "' directory does not exist")
        sys.exit(-1)
    os.chdir(experiments_dir)
    lus_files = glob.glob("*.lus")
    if len(lus_files) == 0:
        print("No Lustre files found in '" + experiments_dir + "' directory")
        sys.exit(-1)
    os.chdir("..")


#run executable in kind .........................


    os.chdir(implement_dir)

    for i, lus_file in enumerate(lus_files):
        sys.stdout.write("({} of {}) {} [".format(i+1, len(lus_files), lus_file))
        sys.stdout.flush()
        run_executables(os.path.splitext(lus_file)[0])

        empty = []
        empty.append(os.path.splitext(lus_file)[0]+".c")
        NestList_size_name_var.append(empty)
    

        sys.stdout.write(".")
        sys.stdout.flush()
        sys.stdout.write("]\n")
        sys.stdout.flush()

    os.chdir("..")
    os.chdir("..")


#run executable in fixpoint .........................


    os.chdir(another_implement_dir)

    for i, lus_file in enumerate(lus_files):
        sys.stdout.write("({} of {}) {} [".format(i+1, len(lus_files), lus_file))
        sys.stdout.flush()
        run_executables(os.path.splitext(lus_file)[0])

        #empty = []
        #empty.append(os.path.splitext(lus_file)[0]+".c")
        #NestList_size_name.append(empty)
    

        sys.stdout.write(".")
        sys.stdout.flush()
        sys.stdout.write("]\n")
        sys.stdout.flush()






    os.chdir("..")
    os.chdir("..")

    print("path =" + os.getcwd())



#################################################################################################
#################################################################################################
#################################################################################################


# jkind_jar = None
# path = os.environ.get("JKIND_HOME") or os.environ.get("PATH") or os.environ.get("path")

# for dir in path.split(':'):
#     jar = os.path.join(dir, "jkind.jar")
#     if os.path.exists(jar):
#         jkind_jar = jar
#         break
# if jkind_jar is None:
#     print("Unable to find jkind.jar in JKIND_HOME or PATH environment variables")
#     sys.exit(-1)
# print("Using JKind: " + jkind_jar)


# smtlib2c_jar = None
# path = os.environ.get("PATH") or os.environ.get("path")

# for dir in path.split(':'):
#     jar = os.path.join(dir, "SMTLib2C.jar")
#     if os.path.exists(jar):
#         smtlib2c_jar = jar
#         break
# if smtlib2c_jar is None:
#     print("Unable to find SMTLib2C.jar in PATH environment variables")
#     sys.exit(-1)

# print("Using SMTLib2C: " + smtlib2c_jar)


# ##############################################################
# execute(EXPERIMENTS_DIR, PUSH_PATH, ANOTHER_PUSH_PATH, IMPLEMENT_DIR, ANOTHER_IMPLEMENT_DIR, NestList_size_name_verification)
# execute(SECOND_EXPERIMENTS_DIR, PUSH_PATH, ANOTHER_PUSH_PATH, SECOND_IMPLEMENT_DIR,SECOND_ANOTHER_IMPLEMENT_DIR, NestList_size_name_smaccm)


# #fill the NestList_overhead
# parse("debug_jkind.txt", "overhead.txt")
# writeOverhead(NestList_overhead, "overhead.txt")
# drawOverhead()
# print("NestList_overhead")
# print(NestList_overhead)

# print()

# #print("NestList_size_name_verification")
# #print(NestList_size_name_verification)
# #print("NestList_size_name_smaccm")
# #print(NestList_size_name_smaccm)


# print("current path =" + os.getcwd())

# #create both verification (kind and fixpoint) loc.txt 
# measureSizeOfC(IMPLEMENT_DIR, NestList_size_name_verification)
# measureSizeOfC(ANOTHER_IMPLEMENT_DIR, NestList_size_name_verification)
# #create both smaccm (kind and fixpoint) loc.txt
# measureSizeOfC(SECOND_IMPLEMENT_DIR, NestList_size_name_smaccm)
# measureSizeOfC(SECOND_ANOTHER_IMPLEMENT_DIR, NestList_size_name_smaccm)

# #append to NestList_size
# combineSizeTxt(IMPLEMENT_DIR+"/loc.txt", ANOTHER_IMPLEMENT_DIR+"/loc.txt")
# combineSizeTxt(SECOND_IMPLEMENT_DIR+"/loc.txt", SECOND_ANOTHER_IMPLEMENT_DIR+"/loc.txt")

# print("NestList_size")
# print(NestList_size)

# drawSize()
# print()

# #append to NestList_performance
# combineResultTxt(IMPLEMENT_DIR+"/results.txt",ANOTHER_IMPLEMENT_DIR+"/results.txt")
# combineResultTxt(SECOND_IMPLEMENT_DIR+"/results.txt",SECOND_ANOTHER_IMPLEMENT_DIR+"/results.txt")

# print("NestList_performance")
# print(NestList_performance)

# drawPerformance()







