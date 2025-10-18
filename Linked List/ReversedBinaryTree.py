class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def reverse_list(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    #Explicacion del metodo Recursivo
    def reverse_list_recursive(self, head: ListNode) -> ListNode:

        #Si la lista no tiene ningun valor esta es la opcion de salida por defecto.
        if not head:
            return None

        #Aqui vamos a regresar los valores de la lista
        newHead = head

        #Si la lista esta apuntando a otro valor
        if head.next:
            #obtenemos el valor al que esta apuntando
            newHead = self.reverse_list_recursive(head.next)

            #Hacemos que el valor que esta al final se vuelva el valor actual
            head.next.next = head

        #Rompemos el enlace con los valores anteriores, ejemplo: 1 -> 2 -> 1 = 2 -> 1
        head.next = None

        return newHead

    @staticmethod
    def print_list(node):
        while node:
            print(node.val, end=" -> ")
            node = node.next
        print("None")

head = ListNode(1)
head.next = ListNode(2)

sol = Solution()
#reverse_head = sol.reverse_list(head)
#Solution.print_list(reverse_head)

reverse_head_recursive = sol.reverse_list_recursive(head)
Solution.print_list(reverse_head_recursive)