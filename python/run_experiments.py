import subprocess
import sys
import os
SIZES = [200,400,600,800,1000,1200,1400,1600]
THREADS = [1,2,3,4,6,7,8]
REPEATS = 3
DATA_DIR = "../data"
EXE_PATH = "../data/matrix.exe"

def generate_matrices(n):
    subprocess.run([sys.executable ,"generate.py",str(n)],check=True,cwd=DATA_DIR)

def run_matrix(threads):
    result = subprocess.run([os.path.abspath(EXE_PATH),str(threads)],capture_output=True,text=True,check=True,cwd=DATA_DIR)
    for line in result.stdout.split("\n"):
        if "time_ms=" in line:
            return int(line.split("time_ms=")[1])
    raise RuntimeError(f"Не распарсил: {result.stdout}")

def verify_result():
    result = subprocess.run(
        [sys.executable, "verify.py"],
        capture_output=True,
        text=True,
        cwd=DATA_DIR
    )
    return "OK" in result.stdout

def main():
    results = []
    for n in SIZES:
        print(f"\n=== N={n} ===")
        generate_matrices(n)
        for threads in THREADS:
            times = []
            for _ in range(REPEATS):
                times.append(run_matrix(threads))
            ok = verify_result()
            min_time = min(times)
            results.append((n, threads, min_time))
            print(f"  threads={threads}: min={min_time} мс, verify={'OK' if ok else 'FAIL'}")
    
    with open("../results.txt", "w", encoding="utf-8") as f:
        f.write("N threads time_ms\n")
        for n, t, time_ms in results:
            f.write(f"{n} {t} {time_ms}\n")
    print("\nГотово!")


if __name__ == "__main__":
    main()
