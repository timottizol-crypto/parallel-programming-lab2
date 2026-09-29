import matplotlib.pyplot as plt
import os


SIZES_FILE = "../results.txt"
IMG_DIR = "../img"
THREADS_LIST = [1, 2, 3, 4, 6, 7, 8]


def read_results(filename: str) -> dict:
    data = {}
    with open(filename, "r", encoding="utf-8") as f:
        next(f)  
        for line in f:
            parts = line.strip().split()
            if len(parts) < 3:
                continue
            n = int(parts[0])
            threads = int(parts[1])
            time_ms = int(parts[2])

            if n not in data:
                data[n] = {}
            data[n][threads] = time_ms
    return data


def plot_time(data: dict) -> None:
    plt.figure(figsize=(10, 6))

    sizes = sorted(data.keys())
    for threads in THREADS_LIST:
        times = [data[n].get(threads) for n in sizes]
        plt.plot(sizes, times, marker="o", label=f"{threads} потоков")

    plt.xlabel("Размер матрицы N")
    plt.ylabel("Время, мс")
    plt.title("Зависимость времени от размера и числа потоков")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, "time_graph.png"), dpi=150)
    plt.close()
    print("Сохранён time_graph.png")


def plot_speedup(data: dict) -> None:
    plt.figure(figsize=(10, 6))

    sizes = sorted(data.keys())
    for threads in THREADS_LIST:
        speedup = [data[n][1] / data[n][threads] for n in sizes]
        plt.plot(sizes, speedup, marker="o", label=f"{threads} потоков")

    plt.xlabel("Размер матрицы N")
    plt.ylabel("Ускорение (Speedup)")
    plt.title("Зависимость ускорения от размера и числа потоков")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, "speedup_graph.png"), dpi=150)
    plt.close()
    print("Сохранён speedup_graph.png")


def plot_efficiency(data: dict) -> None:
    plt.figure(figsize=(10, 6))

    sizes = sorted(data.keys())
    for threads in THREADS_LIST:
        efficiency = [data[n][1] / data[n][threads] / threads for n in sizes]
        plt.plot(sizes, efficiency, marker="o", label=f"{threads} потоков")

    plt.xlabel("Размер матрицы N")
    plt.ylabel("Эффективность")
    plt.title("Зависимость эффективности от размера и числа потоков")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, "efficiency_graph.png"), dpi=150)
    plt.close()
    print("Сохранён efficiency_graph.png")


def main() -> None:
    os.makedirs(IMG_DIR, exist_ok=True)  # создаём папку, если нет

    data = read_results(SIZES_FILE)
    print(f"Прочитано {len(data)} размеров")

    plot_time(data)
    plot_speedup(data)
    plot_efficiency(data)

    print("\nВсе графики построены!")


if __name__ == "__main__":
    main()