from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
from anvil import *
import anvil.server

class Form1(Form1):
    def __init__(self, **properties):
        self.init_components(**properties)

    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    def selection_sort(self, arr):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]
            self.merge_sort(L)
            self.merge_sort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
        return arr

    def button_1_click(self, **event_args):
        input_numbers = self.text_box_1.text.split()
        try:
            numbers = [int(x) for x in input_numbers]
            sorting_algorithm = self.drop_down_1.selected_value
            if sorting_algorithm == "Insertion Sort":
                sorted_numbers = self.insertion_sort(numbers)
            elif sorting_algorithm == "Selection Sort":
                sorted_numbers = self.selection_sort(numbers)
            elif sorting_algorithm == "Bubble Sort":
                sorted_numbers = self.bubble_sort(numbers)
            elif sorting_algorithm == "Merge Sort":
                sorted_numbers = self.merge_sort(numbers)
            self.label_1.text = "Dãy số đã sắp xếp: " + ' '.join(map(str, sorted_numbers))
        except ValueError:
            self.label_1.text = "Vui lòng nhập dãy số nguyên cách nhau bằng khoảng trắng!"

# Khởi tạo ứng dụng và chạy
