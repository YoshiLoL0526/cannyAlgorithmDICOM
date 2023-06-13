#Algoritmo de Canny:
El algoritmo Canny es un algoritmo popular de detección de bordes utilizado en el procesamiento de imágenes para detectar bordes en imágenes digitales. El algoritmo fue desarrollado por John F. Canny en 1986 y es ampliamente utilizado en aplicaciones de visión por computadora. Es un proceso de múltiples etapas que involucra varios pasos:
1. Suavizado gaussiano: En este paso, la imagen se convoluciona con un filtro gaussiano para reducir el ruido y eliminar pequeños detalles.
2. Cálculo del gradiente: El siguiente paso implica calcular el gradiente de la imagen utilizando el operador Sobel. Esto ayuda a identificar áreas de cambio rápido en la intensidad, que corresponden a bordes.
3. Supresión de no máximos: En este paso, el algoritmo busca máximos locales en la magnitud del gradiente y suprime todos los demás valores en la misma dirección. Esto ayuda a afinar los bordes y hacerlos más precisos.
4. Doble umbral: La magnitud del gradiente se divide en dos umbrales para identificar bordes fuertes y débiles. Los bordes fuertes son aquellos con valores de magnitud de gradiente altos, mientras que los bordes débiles tienen valores más bajos. Luego, el algoritmo sigue los bordes fuertes y marca los bordes débiles adyacentes como parte del borde.
5. Seguimiento de borde por histéresis: En este paso final, el algoritmo sigue los bordes y conecta los bordes débiles adyacentes que están conectados a bordes fuertes. Esto ayuda a llenar los espacios vacíos y producir un borde continuo.

##Artículo:
https://ieeexplore.ieee.org/abstract/document/9596109

###Resumen del artículo:
Un sistema de detección de carriles es el componente más importante de un sistema de cálculo de transporte autónomo. Maneja diversos escenarios complejos, como la curvatura del carril, el desgaste de la marca del carril, el cambio de carril, los giros en U, el final y la separación de líneas. Muchas corporaciones y empresas modernas, como Tesla, han logrado la automatización parcial de segundo grado a nivel comercial. En este artículo de investigación, se propone un método de detección de carriles mejorado y optimizado mediante el algoritmo de detección de bordes Canny de OpenCV. Un método rápido y robusto que puede detectar fácilmente carriles en una transmisión de video en vivo o pregrabada. Este marco propuesto combina eficazmente el algoritmo de bordes Canny de OpenCV con la función de transformación de Hough para que pueda aplicarse en aplicaciones a pequeña escala específicamente para carritos de visitantes en un complejo de apartamentos. Las pruebas y el análisis del programa muestran que el software propuesto es muy confiable.

####Referencias:
1. Xu Zhao, Xu Baojie and Wu Guoxin, "Canny edge detection based on Open CV", 2017 13th IEEE international conference on electronic measurement & instruments (ICEMI), 2017.
2. Cao Jianfang, Lichao Chen, Min Wang and Yun Tian, "Implementing a parallel image edge detection algorithm based on the Otsu-canny operator on the Hadoop platform", Computational intelligence and neuroscience 2018, 2018.
3. Rong Weibin et al., "An improved CANNY edge detection algorithm", 2014 IEEE international conference on mechatronics and automation, 2014.
4. Xie Guobo and Wen Lu, "Image edge detection based on opencv", International Journal of Electronics and Electrical Engineering, vol. 1.2, pp. 104-106, 2013.
5. Iqbal Waheed, Iqbal Bilal, Khan Nazar, Mahmood Arif and Erradi Abdelkarim, "Canny edge detection and Hough transform for high resolution video streams using Hadoop and Spark", Cluster Computing, 2020.
6. Zhao Kai et al., "Deep hough transform for semantic line detection", IEEE Transactions on Pattern Analysis and Machine Intelligence, 2021.
7. Cai-Xia Deng, Gui-Bin Wang and Xin-Rui Yang, "Image edge detection algorithm based on improved canny operator", 2013 International Conference on Wavelet Analysis and Pattern Recognition, 2013.
8. Cao Jianfang et al., ". Edge Connection based Canny Edge Detection Algorithm", Computational intelligence and neuroscience, 2018.
9. Z. Kim, "Robust Lane Detection and Tracking in Challenging Scenarios", IEEE Transactions on Intelligent Transportation Systems, vol. 9, no. 1, pp. 16-26, March 2008.
10. I. Culjak, D. Abram, T. Pribanic, H. Dzapo and M. Cifrek, "A brief introduction to OpenCV", 2012 Proceedings of the 35th International Convention MIPRO, pp. 1725-1730, 2012.
11. Wang Yue, Eam Khwang Teoh and Dinggang Shen, "Lane detection and tracking using B-Snake", Image and Vision computing, vol. 22.4, 2004.
12. Aharon Bar Hillel et al., "Recent progress in road and lane detection: a survey", Machine vision and applications, vol. 25.3, no. 2014.
13. Abdulhakam AM Assidiq et al., "Real time lane detection for autonomous vehicles", 2008 International Conference on Computer and Communication Engineering, 2008.
14. Xie Saining and Zhuowen Tu, "Holistically-nested edge detection", Proceedings of the IEEE international conference on computer vision, pp. 1395-1403, 2015.
15. Zhou Junxiao, Haoliang Qian, Ching-Fu Chen, Junxiang Zhao, Guangru Li, Qianyi Wu, et al., "Optical edge detection based on high-efficiency dielectric metasurface", Proceedings of the National Academy of Sciences, vol. 116, no. 23, pp. 11137-11140, 2019.
16. Mittal Mamta, Amit Verma, Iqbaldeep Kaur, Bhavneet Kaur, Meenakshi Sharma, Lalit Mohan Goyal, et al., "An efficient edge detection approach to provide better edge connectivity for image analysis", IEEE access, vol. 7, pp. 33240-33255, 2019.
17. Ren Hongdou, Shengmei Zhao and Jozef Gruska, "Edge detection based on single-pixel imaging", Optics express, vol. 26, no. 5, pp. 5501-5511, 2018.
18. Tahmid Taqi and Eklas Hossain, "Density based smart traffic control system using canny edge detection algorithm for congregating traffic information", 2017 3rd International Conference on Electrical Information and Communication Technology (EICT), 2017.