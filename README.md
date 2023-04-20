# Ponderada 1 | desenho com turtlesim

Esta ponderada requisitava a criação de um nó que controlasse o movimento da tartaruga do nó do turtlesim, fazendo, com isso, um desenho de autoria própria. Para isso, foi necessário, primeiramente, baixar o Ubuntu 22.04 pela Microsoft Store e depois instalar o ROS 2 e suas dependências via apt get. Feito isso, executei o seguinte:

1. Criei um diretório chamado "desenho";
2. Criei uma subpasta chamada "src";
3. Adicionei um script de desenho denominado "turtle_drawing.py"
4. Criei um pacote nessa pasta raiz ("desenho") com "ros2 pkg create --build-type ament_python desenho"
5. Atualizei as dependências nos arquivos de 
6. Construí o pacote com o comando "colcon build --packages-select desenho"
7. Abri um novo terminal para rodar o turtlesim com "ros2 run turtlesim turtlesim_node"
8. No terminal antigo, rodei o script de desenho com "ros2 run desenho desenho"

O script em si, por sua vez, importa a classe de Node e o Twist para criação de mensagens geométricas. Então, criamos um classe herdeira de Node para controlar o movimento da tartaruga. Nela, dentro da construtora, criamos um timer que roda a função de movimento da tartaruga a cada 0,1 segundos. Essa função utiliza um contador para intercalar três tipos de movimento diferentes, cada um com suas componentes de velocidade especificadas em suas respectivas funções. 

A função main inicia o controlador e depois destrói o nó.

Link para vídeo de funcionamento: https://youtu.be/gLbJrfWoiFk
