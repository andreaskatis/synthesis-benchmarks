def run_realizability_fixpoint_only(file_path):
    #delete "xml"
    args = ['java', '-jar', jkind_jar, '-jrealizability',
            '-timeout', '1000', '-n', '1000000', file_path]
    with open(EXTRA_EXPERIMENTS_DIR+"/debug_jkind.txt", "a") as debug:
        debug.write("Running jkind with arguments: {}\n".format(args))
        proc = subprocess.Popen(args, stdout=debug)
        proc.wait()
        debug.write("\n")

def run_synthesis_fixpoint_only(file_path):
    args = ['java', '-jar', jkind_jar, '-jrealizability',
            '-synthesis', '-timeout', '1000', '-n', '1000000', file_path]
    with open(EXTRA_EXPERIMENTS_DIR+"/debug_jkind.txt", "a") as debug:
        debug.write("Running jkind with arguments: {}\n".format(args))
        proc = subprocess.Popen(args, stdout=debug)
        proc.wait()
        debug.write("\n")

def run_fixpoint_fixpoint_only(file_path):
    args = ['java', '-jar', jkind_jar, '-jrealizability',
            '-fixpoint', '-timeout', '1000', '-n', '1000000', file_path]
    with open(EXTRA_EXPERIMENTS_DIR+"/debug_jkind.txt", "a") as debug:
        debug.write("Running jkind with arguments: {}\n".format(args))
        proc = subprocess.Popen(args, stdout=debug)
        proc.wait()
        debug.write("\n")


def run_realizability_synthesis_fixpoint_only(lus_file, experiments_dir): 

    lus_path = os.path.join(experiments_dir, lus_file)
    run_realizability_fixpoint_only(lus_path)
    sys.stdout.write(".")
    sys.stdout.flush()

    lus_path = os.path.join(experiments_dir, lus_file)
    run_synthesis_fixpoint_only(lus_path)
    sys.stdout.write(".")
    sys.stdout.flush()

def run_last_fixpoint_fixpoint_only(lus_file, experiments_dir):  
    lus_path = os.path.join(experiments_dir, lus_file)
    run_fixpoint_fixpoint_only(lus_path)
    sys.stdout.write(".")
    sys.stdout.flush()



def execute_fixpoint_only():
    print("enter fixpoint_only")

    if not os.path.exists(EXTRA_EXPERIMENTS_DIR):
        print("'" + EXTRA_EXPERIMENTS_DIR + "' directory does not exist")
        sys.exit(-1)
    os.chdir(EXTRA_EXPERIMENTS_DIR)
    lus_files = glob.glob("*.lus")
    if len(lus_files) == 0:
        print("No Lustre files found in '" + EXTRA_EXPERIMENTS_DIR + "' directory")
        sys.exit(-1)
    os.chdir("..")

#exeute...................................................
    if ((len(sys.argv)>1) and (sys.argv[1] == "-skipjkind")):
        print("skip the jkind")

    else:
        for i, lus_file in enumerate(lus_files):
            file.write(lus_file+"\n")

            sys.stdout.write("({} of {}) {} [".format(i+1, len(lus_files), lus_file))
            sys.stdout.flush()

            run_realizability_synthesis_fixpoint_only(lus_file, EXTRA_EXPERIMENTS_DIR)
            os.chdir(EXTRA_EXPERIMENTS_DIR)
            move_impl(PUSH_PATH, EXTRA_EXPERIMENTS_DIR)
            os.chdir("..")
    
            run_last_fixpoint_fixpoint_only(lus_file, EXTRA_EXPERIMENTS_DIR)
            os.chdir(EXTRA_EXPERIMENTS_DIR)
            move_impl(ANOTHER_PUSH_PATH, EXTRA_EXPERIMENTS_DIR)
            os.chdir("..")


            sys.stdout.write("]\n")
            sys.stdout.flush()

#do the run_smtlib2c.................................................

    print("Running run_smtlib2c")
#execute run_smtlib2c in kind
    if not os.path.exists(EXTRA_IMPLEMENT_DIR):
        print("'" + EXTRA_IMPLEMENT_DIR + "' directory does not exist")
        sys.exit(-1)
    os.chdir(EXTRA_IMPLEMENT_DIR)
    impl_files = glob.glob("*_skolem.smt2")
    if len(impl_files) == 0:
        print("No Skolem files found in '" + EXTRA_IMPLEMENT_DIR + "' directory")
        sys.exit(-1)
    os.chdir("..")
    os.chdir("..")

    


    for i, impl_file in enumerate(impl_files):
        sys.stdout.write("({} of {}) {} [".format(i+1, len(impl_files), impl_file))
        sys.stdout.flush()
        run_smtlib2c(impl_file, EXTRA_IMPLEMENT_DIR)
        sys.stdout.write(".")
        sys.stdout.flush()
        sys.stdout.write("]\n")
        sys.stdout.flush()


#execute run_smtlib2c in fixpoint

    if not os.path.exists(EXTRA_ANOTHER_IMPLEMENT_DIR):
        print("'" + EXTRA_ANOTHER_IMPLEMENT_DIR + "' directory does not exist")
        sys.exit(-1)
    os.chdir(EXTRA_ANOTHER_IMPLEMENT_DIR)
    impl_files = glob.glob("*_skolem.smt2")
    if len(impl_files) == 0:
        print("No Skolem files found in '" + EXTRA_ANOTHER_IMPLEMENT_DIR+ "' directory")
        sys.exit(-1)
    os.chdir("..")
    os.chdir("..")

    


    for i, impl_file in enumerate(impl_files):
        sys.stdout.write("({} of {}) {} [".format(i+1, len(impl_files), impl_file))
        sys.stdout.flush()
        run_smtlib2c(impl_file, EXTRA_ANOTHER_IMPLEMENT_DIR)
        sys.stdout.write(".")
        sys.stdout.flush()
        sys.stdout.write("]\n")
        sys.stdout.flush()



    print("Running run_make")

    if not os.path.exists(EXTRA_EXPERIMENTS_DIR):
        print("'" + EXTRA_EXPERIMENTS_DIR+ "' directory does not exist")
        sys.exit(-1)
    os.chdir(EXTRA_EXPERIMENTS_DIR)
    lus_files = glob.glob("*.lus")
    if len(lus_files) == 0:
        print("No Lustre files found in '" + EXTRA_EXPERIMENTS_DIR + "' directory")
        sys.exit(-1)
    os.chdir("..")



#execute run_make in kind..................................

    os.chdir(EXTRA_IMPLEMENT_DIR)
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

    os.chdir(EXTRA_ANOTHER_IMPLEMENT_DIR)
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

    if not os.path.exists(EXTRA_EXPERIMENTS_DIR):
        print("'" + EXTRA_EXPERIMENTS_DIR + "' directory does not exist")
        sys.exit(-1)
    os.chdir(EXTRA_EXPERIMENTS_DIR)
    lus_files = glob.glob("*.lus")
    if len(lus_files) == 0:
        print("No Lustre files found in '" + EXTRA_EXPERIMENTS_DIR + "' directory")
        sys.exit(-1)
    os.chdir("..")

#run executable in kind .........................
    os.chdir(EXTRA_IMPLEMENT_DIR)

    for i, lus_file in enumerate(lus_files):
        sys.stdout.write("({} of {}) {} [".format(i+1, len(lus_files), lus_file))
        sys.stdout.flush()
        run_executables(os.path.splitext(lus_file)[0])
        sys.stdout.write(".")
        sys.stdout.flush()
        sys.stdout.write("]\n")
        sys.stdout.flush()

    os.chdir("..")
    os.chdir("..")

#run executable in fixpoint .........................
    os.chdir(EXTRA_ANOTHER_IMPLEMENT_DIR)

    for i, lus_file in enumerate(lus_files):
        sys.stdout.write("({} of {}) {} [".format(i+1, len(lus_files), lus_file))
        sys.stdout.flush()
        run_executables(os.path.splitext(lus_file)[0])
        sys.stdout.write(".")
        sys.stdout.flush()
        sys.stdout.write("]\n")
        sys.stdout.flush()

    os.chdir("..")
    os.chdir("..")
    
