/*
 * Here is class of QUEUE using array
 */
#include <stdio>
#include <system_error>
namespace mysnippets
{
  /* Class for QUEUE using array */
  class ArrayQueue{
  private:
    // TODO: data type obnoxious
    /* Internal storage (array) for queue */
    int *a;
  protected:
    /* Anchors for queue operations */
    int front = 0, rear = 0;
  public:
    ArrayQueue (const int size);
    ~ArrayQueue (void);

    /* Enqueue and dequeue operation for the queue */
    void enqueue (const int data);
    int dequeue (void);

    /* Auxilary useful operation for the queue */
    bool isEmpty (void);
    bool isFull (void);
  }
}
