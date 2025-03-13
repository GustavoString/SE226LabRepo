#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;
};

class Stack {
private:
    Node* head;     // Points to top element of stack.
    int num;        // Number of elements (index-style tracking).
    int capacity;   // Fixed size limit (resized when full).

public:
    Stack(int initialCapacity) {  // You can set any initial size.
        head = nullptr;
        num = -1;
        capacity = initialCapacity;
    }
    void push(int x) {
        if (num == capacity) {
            increaseCapacity();
        }

        Node* newNode = new Node();
        newNode->data = x;

        newNode->next = head;
        head = newNode;

        num++;
    }

    int pop() {
        if (isEmpty()) {
            cout << "Stack is empty." << endl;
            return -1;
        }
        int x = head->data;
        Node* temp = head;
        head = head->next;
        delete temp;
        num--;
        return x;
    }
    int peek() {
        if (isEmpty()) {
            cout << "Stack is empty." << endl;
            return -1;
        }
        return head->data;
    }

    bool isEmpty() {
        return num < 0;
    }

    void increaseCapacity() {
        capacity *= 2;
    }

    bool deleteElement(int val) {
        int counter = num;
        Node* temp = head;
        Node* prev = nullptr;

        while (counter >= 0) {
            if (temp->data == val) {
                if (prev == nullptr) {
                    head = temp->next;
                } else {
                    prev->next = temp->next;
                }

                delete temp;
                num--;
                return true;
            }

            prev = temp;
            temp = temp->next;
            counter--;
        }

        return false;
    }
};

int main() {
    Stack* stack = new Stack(10);
    cout << "Empty: " << stack->isEmpty() << endl;

    cout << "Pushing 1 through 10..." << endl;
    stack->push(1);
    stack->push(2);
    stack->push(3);
    stack->push(4);
    stack->push(5);
    stack->push(6);
    stack->push(7);
    stack->push(8);
    stack->push(9);
    stack->push(10);

    cout << "Empty: " << stack->isEmpty() << endl;

    cout << "Peek: " << stack->peek() << endl;
    cout << "Popped: " << stack->pop() << endl;
    cout << "Popped: " << stack->pop() << endl;
    cout << "Popped: " << stack->pop() << endl;
    cout << "Popped: " << stack->pop() << endl;

    cout << "Deleting 4: " << stack->deleteElement(4) << endl;
    cout << "Deleting 8: " << stack->deleteElement(8) << endl;
    cout << "Peek: " << stack->peek() << endl;
    cout << "Popped: " << stack->pop() << endl;
    cout << "Popped: " << stack->pop() << endl;
    cout << "Popped: " << stack->pop() << endl;
    cout << "Popped: " << stack->pop() << endl;
    cout << "Popped: " << stack->pop() << endl;
    cout << "Popped: " << stack->pop() << endl;

    cout << "Empty: " << stack->isEmpty() << endl;

    cout << "Pushing over current capacity..." << endl;
    stack->push(1);
    stack->push(2);
    stack->push(3);
    stack->push(4);
    stack->push(5);
    stack->push(6);
    stack->push(7);
    stack->push(8);
    stack->push(9);
    stack->push(10);
    stack->push(11);
    stack->push(12);
    stack->push(13);
    stack->push(14);
    stack->push(15);
    cout << "Empty: " << stack->isEmpty() << endl;

    cout << "Peek: " << stack->peek() << endl;
    cout << "Popped: " << stack->pop() << endl;
    cout << "Popped: " << stack->pop() << endl;
    cout << "Popped: " << stack->pop() << endl;
    cout << "Popped: " << stack->pop() << endl;
    cout << "Popped: " << stack->pop() << endl;
    cout << "Popped: " << stack->pop() << endl;
    cout << "Popped: " << stack->pop() << endl;
    cout << "Popped: " << stack->pop() << endl;
    cout << "Popped: " << stack->pop() << endl;


    cout << "Deleting 4: " << stack->deleteElement(4) << endl;
    cout << "Deleting 360: " << stack->deleteElement(360) << endl;



    delete stack;
    return 0;
}