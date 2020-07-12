###################################################
# Título: Gráfico de comparação de fluxo difusivo #
# Autor: Marcelo Di Lello Jordão                  #
# email: dilellocn@gmail.com                      #
###################################################

# -*- coding: utf-8 -*-

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import numpy as np
import pandas as pd
from datetime import datetime


# Controle de fonte
tamanho = 12
plt.close('all')
plt.rc('text', usetex = False)
plt.rc('font', family = 'sans-serif')
plt.rc('font', serif = 'Calibri')
plt.rc('legend',fontsize = tamanho)
plt.rc('font', size = tamanho)         
plt.rc('axes', titlesize = tamanho)    
plt.rc('axes', labelsize = tamanho)   
plt.rc('xtick', labelsize = tamanho)  
plt.rc('ytick', labelsize = tamanho)
plt.rc('figure', titlesize = tamanho) 

# Variáveis de entrada
ch4_flux_pre = np.loadtxt("/home/marcelo/Documentos/projects/TXT/flux_pre.txt") # fluxo difusivo de mentano pre-enchimento
ch4_flux_pos = np.loadtxt("/home/marcelo/Documentos/projects/TXT/flux_pos.txt") # fluxo difusivo de metano pos-enchimento
labelx = ['CAM 22', 'CAM 49', 'CAM 48', 'CAM 14', 'CAM 23.2', 'CAM 23.1', 'CAM 27', 'CAM 15', 'CAM 13', 'CAM 33', 'CAM 32', 'CAM 41', 'CAM S11', 'CAM 29', 'CAM S9', 'CAM S41', 'CAM 4', 'CAM S8.2', 'CAM 3', 'CAM S3', 'CAM 7', 'CAM S17', 'CAM S2', 'CAM 8', 'CAM S6.3', 'CAM S1.1', 'CAM 55', 'CAM S21', 'CAM 4.2', 'CAM S6', 'CAM S3', 'CAM 44', 'CAM 2', 'CAM 1', 'CAM S1.2']# código dos pontos de coleta que aparecerão no eixo x

# Gráfico de fluxo difusivo de metano
fig, (ax, ax2) = plt.subplots(2, 1, sharex = True) # dimensiona o gráfico
x = np.arange(len(labelx))  # define localização dos códigos dos pontos de coleta no eixo x
y = np.array([100, 1000, 2000, 3000, 4000, 5000]) # define localização das labels do eixo y acima da quebra de escala
width = 0.3  # largura da barra
labelch4 = ['100','1.000','2.000','3.000','4.000','5.000'] # correção da notação de separador de milhares e/ou decimal
d = .005 # tamanho do traço em diagonal que marca a quebra de escala do eixo y
ax.bar(x - width/2, ch4_flux_pre, width, label='Pré-enchimento: 11/2011', color = 'g') # define a barra pré-enchimento acima da quebra de escala do eixo y
ax.bar(x + width/2, ch4_flux_pos, width, label='Pós-enchimento: 11/2012', color = 'r', alpha=0.7) # define a barra pós-enchimento abaixo da quebra de escala do eixo y
ax2.bar(x - width/2, ch4_flux_pre, width, color = 'g') # define a barra pré-enchimento acima da quebra de escala do eixo y
ax2.bar(x + width/2, ch4_flux_pos, width, color = 'r',alpha=0.7) # define a barra pós-enchimento abaixo da quebra de escala do eixo y
ax.axvspan(-0.40, 2.45, facecolor='b', alpha=0.10) # define o retângulo que agrupa os pontos no trecho afluente acima da quebra de escala do eixo y
ax2.axvspan(-0.40, 2.45, facecolor='b', alpha=0.10) # define o retângulo que agrupa os pontos no trecho afluente abaixo da quebra de escala do eixo y
ax.axvspan(11.55, 31.45, facecolor='b', alpha=0.10)  # define o retângulo que agrupa os pontos no trecho do reservatório acima da quebra de escala do eixo y
ax2.axvspan(11.55, 31.45, facecolor='b', alpha=0.10) # define o retângulo que agrupa os pontos no trecho do reservatório abaixo da quebra de escala do eixo y
ax.set_ylabel('Fluxo difusivo de CH'+r'$_{4}$'' (mg.m'+r'$^{-2}$''d'+r'$^{-1}$'')', position= (-10, 0.1)) # define a legenda do eixo y
ax.set_ylim(100, 5000) # define os limites do eixo y acima da quebra de escala
ax.set_yticks(y) # configura a localização dos labels do eixo y acima da quebra de escala 
ax2.set_ylim(-30, 100) # define os limites do eixo y abaixo da quebra de escala
ax.spines['top'].set_visible(False) # configura os spines do topo na parte acima da quebra de escala
ax.spines['bottom'].set_visible(False) # configura os spines da base na parte acima da quebra de escala
ax.xaxis.tick_top()
ax2.spines['top'].set_visible(False) # configura os spines do topo na parte abaixo da quebra de escala
ax.tick_params(labeltop=False)# configura os spines da base na parte abaixo da quebra de escala
ax2.xaxis.tick_bottom()
kwargs = dict(transform=ax.transAxes, color='k', clip_on=False) # construção da diagonal da quebra de escala
ax.plot((-d, +d), (-d, +d), **kwargs) # construção da diagonal da quebra de escala   
ax.plot((1 - d, 1 + d), (-d, +d), **kwargs) # construção da diagonal da quebra de escala
kwargs.update(transform=ax2.transAxes) # construção da diagonal da quebra de escala
ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs) # construção da diagonal da quebra de escala
ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs) # construção da diagonal da quebra de escala
ax.set_xlim(-0.5, 34.5) # define os limites do eixo y
ax2.set_xticks(x) # configura a localização dos labels do eixo x
ax.set_yticklabels(labelch4) # entra com as labels do eixo y acima da quebra de escala
ax2.set_xticklabels(labelx, rotation = 90) # entra com as labels do eixo x na orientação vertical
ax.legend(loc='center') # posiciona a legenda
ax.text(-0.2, 4600, 'Afluente') # posiciona os textos dentro gráfico
ax.text(5, 4600, 'Rio montante') # posiciona os textos dentro gráfico
ax.text(20, 4600, 'Reservatório') # posiciona os textos dentro gráfico
ax.text(32.0, 4600, 'Rio jus.') # posiciona os textos dentro gráfico
ax2.text(5, 5, 'S.D.', color ='r', rotation = 90) # posiciona os textos dentro gráfico
ax2.text(18, 5, 'S.D.', color ='r', rotation = 90) # posiciona os textos dentro gráfico
fig.tight_layout()
plt.subplots_adjust(hspace=0.05)
plt.show()




