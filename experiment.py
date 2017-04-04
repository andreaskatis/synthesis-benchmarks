import os, subprocess, sys, glob, shutil

#
# Configuration
#

EXPERIMENTS_DIR = 'verification'
PUSH_PATH = 'kind'
IMPLEMENT_DIR = 'verification/kind'

#TIMEOUT = 3600

#
# Gather Lustre files
#

if not os.path.exists(EXPERIMENTS_DIR):
    print("'" + EXPERIMENTS_DIR + "' directory does not exist")
    sys.exit(-1)
os.chdir(EXPERIMENTS_DIR)
lus_files = glob.glob("*.lus")
if len(lus_files) == 0:
    print("No Lustre files found in '" + EXPERIMENTS_DIR + "' directory")
    sys.exit(-1)
os.chdir("..")


#
# Find jkind.jar
#

jkind_jar = None
path = os.environ.get("JKIND_HOME") or os.environ.get("PATH") or os.environ.get("path")

for dir in path.split(':'):
    jar = os.path.join(dir, "jkind.jar")
    if os.path.exists(jar):
        jkind_jar = jar
        break
if jkind_jar is None:
    print("Unable to find jkind.jar in JKIND_HOME or PATH environment variables")
    sys.exit(-1)
print("Using JKind: " + jkind_jar)

#
# Run JKind
#
# '-timeout', str(TIMEOUT)
#file_path = verification/car_1.lus

def run_realizability(file_path):
    #delete "xml"
    args = ['java', '-jar', jkind_jar, '-jrealizability',
            '-timeout', '10000', '-n', '1000000', file_path]
    with open("debug_jkind.txt", "a") as debug:
        debug.write("Running jkind with arguments: {}\n".format(args))
        proc = subprocess.Popen(args, stdout=debug)
        proc.wait()
        debug.write("\n")

def run_synthesis(file_path):
    args = ['java', '-jar', jkind_jar, '-jrealizability',
            '-synthesis', '-timeout', '10000', '-n', '1000000', file_path]
    with open("debug_jkind.txt", "a") as debug:
        debug.write("Running jkind with arguments: {}\n".format(args))
        proc = subprocess.Popen(args, stdout=debug)
        proc.wait()
        debug.write("\n")

def run_both(lus_file):

    lus_path = os.path.join(EXPERIMENTS_DIR, lus_file)

    run_realizability(lus_path)
    sys.stdout.write(".")
    sys.stdout.flush()

    lus_path = os.path.join(EXPERIMENTS_DIR, lus_file)
    run_synthesis(lus_path)
    sys.stdout.write(".")
    sys.stdout.flush()

def move_impl():
    impl_files = glob.glob("*.impl")
    print(impl_files[1])
    if len(impl_files) == 0:
        print("No implement files found in '" + EXPERIMENTS_DIR + "' directory")
        sys.exit(-1)

  #  smt_files = glob.glob("*.smt2")
  #  if len(smt_files) == 0:
   #     print("No stm2 files found in '" + EXPERIMENTS_DIR + "' directory")
    #    sys.exit(-1)

#move the impl files to PUSH_PATH
    print("moving impl files")
    for i, impl_file in enumerate(impl_files):
        old_implPath = impl_file
        new_implPath = os.path.join(PUSH_PATH, impl_file)
        shutil.move(old_implPath, new_implPath)

#delete all smt files
    #print("deleting smt2 files")
    #for i, smt_file in enumerate(smt_files):
     #   os.remove(smt_file)




#exeute...................................................

for i, lus_file in enumerate(lus_files):
    sys.stdout.write("({} of {}) {} [".format(i+1, len(lus_files), lus_file))
    sys.stdout.flush()
    run_both(lus_file)
    sys.stdout.write("]\n")
    sys.stdout.flush()

os.chdir(EXPERIMENTS_DIR)
move_impl()



#do the run_smtlib2c.................................................

print("Running run_smtlib2c")

os.chdir("..")
if not os.path.exists(IMPLEMENT_DIR):
    print("'" + IMPLEMENT_DIR + "' directory does not exist")
    sys.exit(-1)
os.chdir(IMPLEMENT_DIR)
impl_files = glob.glob("*.impl")
if len(impl_files) == 0:
    print("No Skolem files found in '" + IMPLEMENT_DIR + "' directory")
    sys.exit(-1)
os.chdir("..")
os.chdir("..")



#
# Find jkind.jar
#

smtlib2c_jar = None
path = os.environ.get("PATH") or os.environ.get("path")

for dir in path.split(':'):
    jar = os.path.join(dir, "SMTLib2C.jar")
    if os.path.exists(jar):
        smtlib2c_jar = jar
        break
if smtlib2c_jar is None:
    print("Unable to find SMTLib2C.jar in PATH environment variables")
    sys.exit(-1)
print("Using SMTLib2C: " + smtlib2c_jar)

#
# Run JKind
#
# '-timeout', str(TIMEOUT)

def run_smtlib2c(impl_file):
    file_path = os.path.join(IMPLEMENT_DIR, impl_file)
    args = ['java', '-jar', smtlib2c_jar,
            '-iter', '1000000',
            '-c_harness', '-lustrec_harness', '-lustrecnode', 'top', file_path]
    with open(IMPLEMENT_DIR+"/debug_smtlib2c.txt", "a") as debug:
        debug.write("Running SMTLib2C with arguments: {}\n".format(args))
        proc = subprocess.Popen(args, stdout=debug)
        proc.wait()
        debug.write("\n")

#execute run_smtlib2c

for i, impl_file in enumerate(impl_files):
    sys.stdout.write("({} of {}) {} [".format(i+1, len(impl_files), impl_file))
    sys.stdout.flush()
    run_smtlib2c(impl_file)
    sys.stdout.write(".")
    sys.stdout.flush()
    sys.stdout.write("]\n")
    sys.stdout.flush()


print("Running run_make")


if not os.path.exists(EXPERIMENTS_DIR):
    print("'" + EXPERIMENTS_DIR + "' directory does not exist")
    sys.exit(-1)
os.chdir(EXPERIMENTS_DIR)
lus_files = glob.glob("*.lus")
if len(lus_files) == 0:
    print("No Lustre files found in '" + EXPERIMENTS_DIR + "' directory")
    sys.exit(-1)
os.chdir("..")


#
# Run JKind
#
# '-timeout', str(TIMEOUT)

def run_makefile(file_path):
    args = ['make', 'FILE='+file_path]
    with open("debug_make.txt", "a") as debug:
        debug.write("Running make for file: {}\n".format(args))
        proc = subprocess.Popen(args, stdout=debug)
        proc.wait()
        debug.write("\n")

#execute run_make..................................

os.chdir(IMPLEMENT_DIR)
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




if not os.path.exists(EXPERIMENTS_DIR):
    print("'" + EXPERIMENTS_DIR + "' directory does not exist")
    sys.exit(-1)
os.chdir(EXPERIMENTS_DIR)
lus_files = glob.glob("*.lus")
if len(lus_files) == 0:
    print("No Lustre files found in '" + EXPERIMENTS_DIR + "' directory")
    sys.exit(-1)
os.chdir("..")


#
# Run JKind
#
# '-timeout', str(TIMEOUT)

def run_executables(file_path):
    args = ['./'+file_path]
    with open("results.txt", "a") as debug:
        proc = subprocess.Popen(args, stdout=debug)
        proc.wait()

os.chdir(IMPLEMENT_DIR)

for i, lus_file in enumerate(lus_files):
    sys.stdout.write("({} of {}) {} [".format(i+1, len(lus_files), lus_file))
    sys.stdout.flush()
    run_executables(os.path.splitext(lus_file)[0])
    sys.stdout.write(".")
    sys.stdout.flush()
    sys.stdout.write("]\n")
    sys.stdout.flush()

































#os.chdir(EXPERIMENTS_DIR)
#xml_files = glob.glob("*.xml")
#for xml_file in xml_files:
#	mv = subprocess.Popen(['mv', xml_file, 'xml'])
#	mv.wait()
