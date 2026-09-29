#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <chrono>
#include <stdexcept>
#include <cstdlib>
using namespace std;
#include <omp.h>

using Matrix = vector<vector<double>>;
Matrix readMatrix(const string& filename) {
	ifstream file(filename);
	if (!file.is_open()) throw runtime_error("Файл A не открылся");
	int n;
	file >> n;
	Matrix matrix(n, vector<double>(n));
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			file >> matrix[i][j];
		}
	}
	file.close();
	return matrix;
}
void writeMatrix(const string& filename, const Matrix& matrix) {
	ofstream file(filename);
	if (!file.is_open()) throw runtime_error("Файл B не открылся");
	int n = matrix.size();
	file << n << "\n";
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				file << matrix[i][j];
				if (j != n - 1)file << " ";
			}
			file << "\n";
		}
		file.close();
}

int main(int argc,char* argv[]) {
	int numThreads = 1;
	if (argc > 1) {
    	numThreads = std::atoi(argv[1]);
	}
omp_set_num_threads(numThreads);
	try {
		Matrix A = readMatrix("A.txt");
		Matrix B = readMatrix("B.txt");
		if (A.size() != B.size()) {
			std::cerr << "Ошибка: размеры матриц не совпадают!\n";
			return 1;
		}
		int n = A.size();
		Matrix C(n, vector<double>(n, 0.0));
		auto start = chrono::high_resolution_clock::now();
		#pragma omp parallel for
		for (int i = 0; i < A.size(); i++) {
			for (int j = 0; j < A.size(); j++) {
				for (int k = 0; k < A.size(); k++) {
					C[i][j] += (A[i][k] * B[k][j]);
				}
			}
		}
		auto end = std::chrono::high_resolution_clock::now();
		auto duration = chrono::duration_cast<chrono::milliseconds>(end - start);
		writeMatrix("C.txt", C);
		cout << "Размер матрицы: " << n << "\n";
		cout << " threads=" << numThreads << " time_ms=" << duration.count() << "\n";

	}
	catch (const std::exception& e) {
		std::cerr << "Ошибка: " << e.what() << "\n";
		return 1;
	}

	return 0;
}