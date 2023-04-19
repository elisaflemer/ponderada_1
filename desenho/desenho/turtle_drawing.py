# Script para controlar o movimento da tartaruga
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

# Classe que controla o movimento da tartaruga
class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller') 
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10) 
        self.timer_ = self.create_timer(0.1, self.move_turtle) # Roda a função move_turtle a cada 0.1 segundos
        self.twist_msg_ = Twist() 
        self.counter = 0 # Contador para controlar o tempo de cada parte do movimento
        self.part = 1 # Variável para controlar a parte do movimento que está sendo executada
        
    # Funções para cada parte do movimento
    def part1(self):
        self.twist_msg_.linear.x = 0.5 
        self.twist_msg_.angular.z = 0.5
        self.publisher_.publish(self.twist_msg_)

    def part2(self):
        self.twist_msg_.linear.x = 1.2
        self.twist_msg_.angular.z = -0.5
        self.publisher_.publish(self.twist_msg_)

    def part3(self):
        self.twist_msg_.linear.x = -1.0
        self.twist_msg_.angular.z = 0.5
        self.publisher_.publish(self.twist_msg_)

    # Função que controla o movimento da tartaruga agregando as diferentes partes
    def move_turtle(self):
        if self.part == 1:
            self.part1()
            self.counter +=1
        elif self.part == 2:
            self.part2()
            self.counter +=1
        else:
            self.part3()
            self.counter +=1
        # Verifica se a parte do movimento já foi executada por 5 segundos
        if (self.counter >= 50):
            if self.part in [1, 2]:
                self.part += 1
            else:
                self.part = 1
            self.counter = 0
    
def main(args=None):
    rclpy.init(args=args)
    turtle_controller = TurtleController()
    rclpy.spin(turtle_controller)
    turtle_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
