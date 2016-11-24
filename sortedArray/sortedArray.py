from typing import Sequence

class SortedArray(object):
    """ Đây là lớp để triển khai các thuật toán sắp xếp cơ bản. """

    def selectionSort(self, arr: Sequence[int]) -> Sequence[int]:
        # Input: Một mảng các phần tử
        # Out put: Mảng được sắp xếp


        # --------Thuật toán sắp xếp lựa chọn.-----


        # Ý tưởng:

        # - Chọn phần tử nhỏ nhất trong N phần tử ban đầu, đưa phần tử này về vị trí đầu dãy hiện hành; sau đó loại nó khỏi
        # danh sách sắp xếp tiếp theo.
        # - Xem dãy hiện hành chỉ còn N-1 phần tử của dãy ban đầu, bắt đầu từ vị trí thứ 2; lặp lại quá trình trên cho dãy hiện
        # hành... đến khi dãy chỉ còn 1 phần tử.

        # Thuật toán:

        # Bước 1: i = 1; // lần đầu tiên xử lý
        # Bước 2: tìm phần tử nhỏ nhất a[min] trong dãy từ a[i] đến a[N]
        # Bước 3: Hoán vị a[min] và a[i]
        # Bước 4: Nếu i< N-1 thì i = i+1; Lặp lại bước 2
        # Ngược lai: Dừng

        return [];

