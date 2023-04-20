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

Em suma, em um terminal, é criado um nó de renderização da tartaruga. Em outro, é criado um nó publicador que, através do ROS2, envia mensagens para o outro nó especificando a velocidade da tartaruga em dado momento. Essa comunicação acontece a cada 10s, segundo o timer criado no nó publicador. Nesse sentido, o nó de controlador age como servidor e o nó do turtlesim age como cliente. Essa comunicação acontece no tópico "turtle1/cmd_vel", na qual o controle é publisher e o turtlesim é subscriber. Logo, é uma comunicação pub-sub.

O desenho em si é fruto da intercalação de três combinações de velocidades linear e angular diferentes. A soma desses movimentos, em grande número, gera uma estrutura gráfica com diversos arcos formando figuras semelhantes a pétalas. Isso é representado no código pela mudança dos inteiros nos argumentos de velocidade linear e angular nos métodos que enviam essas propriedades ao turtlesim.

Link para vídeo de funcionamento: https://youtu.be/gLbJrfWoiFk
