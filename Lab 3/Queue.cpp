
#include <iostream>
#include <queue>

using namespace std;

class Node{
public:
    int value;
    Node* next;

    Node(int data){
        value = data;
        next = nullptr;
    }
};

class Queue {
private:
    Node* front;
    Node* rear;
    int count;

public:
    Queue() {
        front = nullptr;
        rear = nullptr;
        count = 0;
    }

    void enqueue(int value) {
        Node* newNode = new Node(value);
        if (front == nullptr) {
            front = newNode;
            rear = newNode;
        } else {
            rear->next = newNode;
            rear = newNode;
        }
        count++;
    }

    int dequeue() {
        if (front == nullptr) {
            cout << "Queue is empty" << endl;
            return -1;
        }

        Node* temp = front;
        front = front->next;
        int ret = temp->value;
        delete temp;
        count--;

        if (front == nullptr) {
            rear = nullptr;
        }

        return ret;
    }

    int top() {
        return front->value;
    }

    bool isEmpty() {
        return front == nullptr || count == 0;
    }

    int size() {
        return count;
    }
};

int main(){
    Queue* queue = new Queue();

    cout << "Empty: " << queue->isEmpty() << endl;
    cout << "Size: " << queue->size() << endl;

    cout << "Enter how many values you want to enqueue: ";
    int amount;
    cin >> amount;
    for (int i = 0; i < amount; i++) {
        cout << "Enter an integer value: ";
        int input;
        cin >> input;
        queue->enqueue(input);
    }

    cout << "Empty: " << queue->isEmpty() << endl;
    cout << "Size: " << queue->size() << endl;
    cout << "Top: " << queue->top() << endl;

    cout << "Dequeueing..." << endl;
    const int size = queue->size();
    for (int i = 0; i < size; i++) {
        cout << "Dequeued " << queue->dequeue() << endl;
    }

    cout << "Empty: " << queue->isEmpty() << endl;
    cout << "Size: " << queue->size() << endl;

    return 0;
}




