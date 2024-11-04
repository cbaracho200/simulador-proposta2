import streamlit as st
import numpy as np
import pandas as pd
import os
import plotly.express as px
from login import *
import math
from pathlib import Path

st.set_page_config(page_title="VL-App", page_icon="📊",layout="wide", initial_sidebar_state="expanded")
DATA_FILENAME = Path(__file__).parent/'data/gdp_data.csv'

st.divider()
st.title("📊 SIMULADOR DE PROPOSTA - VL")
st.divider()

def real_br_money_mask(valor):
    return f"R$ {valor:,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")


pilar1, pilar2 = st.columns([5, 5])

with pilar1.container(border=True):
    st.html("""
        <style>
            .custom-banner {
                color: white;
                background-color: #006400;
                border-radius: 10px;
                width: 100%;
                padding: 5px;
                margin: 5px auto;
                text-align: center;
                font-size: 14px;
                font-weight: bold;
            }

            /* Media query para telas médias */
            @media (min-width: 768px) {
                .custom-banner {
                    width: 100%;
                }
            }

            /* Media query para telas grandes */
            @media (min-width: 1024px) {
                .custom-banner {
                    width: 100%;
                }
            }
        </style>

        <div class="custom-banner">
            Dados do cliente:
        </div>
    """)
    col1, col2, col3 = st.columns([3, 2, 2])
    with col1:
        st.text_input("Nome do Comprador", value="VALERIA FERREIRA LIRA")
        st.text_input("CPF do Comprador", value="76607718472")
    with col2:
        st.text_input("Data de Nascimento", value="1971-12-31")
        st.text_input("Imobiliária", value="Armando Nogueira")
    with col3:
        st.text_input("Renda Familiar", value="R$ 3,085.00")

    
with pilar1.expander("🔍 Dados do Fiador 1:"):
    st.html("""
        <style>
            .custom-banner {
                color: white;
                background-color: #006400;
                border-radius: 10px;
                width: 100%;
                padding: 5px;
                margin: 5px auto;
                text-align: center;
                font-size: 14px;
                font-weight: bold;
            }

            /* Media query para telas médias */
            @media (min-width: 768px) {
                .custom-banner {
                    width: 100%;
                }
            }

            /* Media query para telas grandes */
            @media (min-width: 1024px) {
                .custom-banner {
                    width: 100%;
                }
            }
        </style>

        <div class="custom-banner">
            Dados do Fiador 1:
        </div>
    """)
    col7, col8 = st.columns(2)
    with col7:
        st.text_input("Nome do Fiador 1")
        st.text_input("CPF Fiador 1")
    with col8:
        st.text_input("Renda Bruta Fiador 1")
        st.text_input("Tipo Renda Fiador 1")

with pilar1.expander("🔍 Dados do Fiador 2:"):
    st.html("""
        <style>
            .custom-banner {
                color: white;
                background-color: #006400;
                border-radius: 10px;
                width: 100%;
                padding: 5px;
                margin: 5px auto;
                text-align: center;
                font-size: 14px;
                font-weight: bold;
            }

            /* Media query para telas médias */
            @media (min-width: 768px) {
                .custom-banner {
                    width: 100%;
                }
            }

            /* Media query para telas grandes */
            @media (min-width: 1024px) {
                .custom-banner {
                    width: 100%;
                }
            }
        </style>

        <div class="custom-banner">
            Dados do Fiador 2:
        </div>
    """)
    col7, col8 = st.columns(2)
    with col7:
        st.text_input("Nome do Fiador 2")
        st.text_input("CPF Fiador 2")
    with col8:
        st.text_input("Renda Bruta Fiador 2")
        st.text_input("Tipo Renda Fiador 2")


with pilar2.container(border=True):
    st.html("""
        <style>
            .custom-banner {
                color: white;
                background-color: #006400;
                border-radius: 10px;
                width: 100%;
                padding: 5px;
                margin: 5px auto;
                text-align: center;
                font-size: 14px;
                font-weight: bold;
            }

            /* Media query para telas médias */
            @media (min-width: 768px) {
                .custom-banner {
                    width: 100%;
                }
            }

            /* Media query para telas grandes */
            @media (min-width: 1024px) {
                .custom-banner {
                    width: 100%;
                }
            }
        </style>

        <div class="custom-banner">
            Dados do empreendimento:
        </div>
    """)
    col4, col5, col6, col7, col8 = st.columns([1, 0.75, 0.5, 0.75, 1])
    with col4:
        st.selectbox("Empreendimento", options=["RVV", "RCQ", "RVR"])

    with col5:
        st.text_input("Bloco", value="Bloco A")

    with col6:
        st.text_input("Unidade", value="101")


    with col7:
        st.text_input("Área Útil", value="57.77")


    with col8:
        st.text_input("Tipologia", value="Unidade Térreo")

    col4, col5, col6 = st.columns([1, 0.75, 0.75])

    with col4:
        st.text_input("Empreendimento / Município", value="Vila Real",disabled=True)
    with col5:
        st.text_input("Assinatura", value="Imediata", disabled=True)

    with col6:
        st.text_input("Valor Imóvel", value="202.000,00", disabled=True)

    col4, col5 = st.columns([0.5, 1 ])

    with col4:
        st.text_input("Valor Tabela", value="201.000,00",disabled=True)
    with col5:
        st.text_input("Observação", value="Sem desconto",disabled=True)


st.html("""
        <style>
            .custom-banner3 {
                color: white;
                background-color: #008080;
                border-radius: 10px;
                width: 100%;
                padding: 5px;
                margin: 5px auto;
                text-align: center;
                font-size: 14px;
                font-weight: bold;
            }

            /* Media query para telas médias */
            @media (min-width: 768px) {
                .custom-banner {
                    width: 100%;
                }
            }

            /* Media query para telas grandes */
            @media (min-width: 1024px) {
                .custom-banner {
                    width: 100%;
                }
            }
        </style>

        <div class="custom-banner3">
            DADOS DO PLANO DE PAGAMENTO::
        </div>
    """)

pilar3, pilar4 = st.columns([5, 5])

with pilar3.container(border=True):
    st.html("""
            <style>
                .custom-banner4 {
                    color: white;
                    background-color: #006400;
                    border-radius: 10px;
                    width: 100%;
                    padding: 5px;
                    margin: 5px auto;
                    text-align: center;
                    font-size: 14px;
                    font-weight: bold;
                }

                /* Media query para telas médias */
                @media (min-width: 768px) {
                    .custom-banner {
                        width: 100%;
                    }
                }

                /* Media query para telas grandes */
                @media (min-width: 1024px) {
                    .custom-banner {
                        width: 100%;
                    }
                }
            </style>

            <div class="custom-banner4">
                IMOBILIARIA:
            </div>
        """)
    ld1, ld2 = st.columns([2,2])
    with ld1:
        premio = st.text_input("Prêmio", value="1500.00")
        comissao = st.text_input("Comissão", value="7516.15")
    with ld2:
        st.text_input("Data Prêmio", value="2024-01-01")
        st.text_input("Data Comissão", value="2024-01-01")
    
    st.text_input("Total", value=float(premio)+float(comissao), disabled=True)


with pilar3.container(border=True):
    st.html("""
            <style>
                .custom-banner4 {
                    color: white;
                    background-color: #006400;
                    border-radius: 10px;
                    width: 100%;
                    padding: 5px;
                    margin: 5px auto;
                    text-align: center;
                    font-size: 14px;
                    font-weight: bold;
                }

                /* Media query para telas médias */
                @media (min-width: 768px) {
                    .custom-banner {
                        width: 100%;
                    }
                }

                /* Media query para telas grandes */
                @media (min-width: 1024px) {
                    .custom-banner {
                        width: 100%;
                    }
                }
            </style>

            <div class="custom-banner4">
                VL CONSTRUTORA:
            </div>
        """)
    ld1, ld2 = st.columns([2,2])
    with ld1:
        sinal = st.text_input("Sinal", value="1500.00")
    with ld2:
        st.text_input("Data Sinal", value="2024-01-01")

with pilar3.container(border=True):
    st.html("""
            <style>
                .custom-banner4 {
                    color: white;
                    background-color: #006400;
                    border-radius: 10px;
                    width: 100%;
                    padding: 5px;
                    margin: 5px auto;
                    text-align: center;
                    font-size: 14px;
                    font-weight: bold;
                }

                /* Media query para telas médias */
                @media (min-width: 768px) {
                    .custom-banner {
                        width: 100%;
                    }
                }

                /* Media query para telas grandes */
                @media (min-width: 1024px) {
                    .custom-banner {
                        width: 100%;
                    }
                }
            </style>

            <div class="custom-banner4">
                FINANCIAMENTO:
            </div>
        """)

    financiamento = st.text_input("Financiamento", value="0.00")
    subsidio = st.text_input("Subsídio", value="0.00")
    fgts = st.text_input("FGTS", value="0.00")
    total_financ = st.text_input("Total CEF", value=real_br_money_mask(float(subsidio)+float(financiamento)+float(fgts)), disabled=True)







with pilar4.container(border=True):
    st.html("""
            <style>
                .custom-banner5 {
                    color: white;
                    background-color: #006400;
                    border-radius: 10px;
                    width: 100%;
                    padding: 5px;
                    margin: 5px auto;
                    text-align: center;
                    font-size: 14px;
                    font-weight: bold;
                }

                /* Media query para telas médias */
                @media (min-width: 768px) {
                    .custom-banner {
                        width: 100%;
                    }
                }

                /* Media query para telas grandes */
                @media (min-width: 1024px) {
                    .custom-banner {
                        width: 100%;
                    }
                }
            </style>

            <div class="custom-banner5">
                POUPANÇA - CURTO PRAZO:
            </div>
        """)

    c0, c1, c2, c3, c4 = st.columns([2, 1,1,1,1])
    with c0:
        st.text_input("Obs Mensais:", value="Máx de R$ 0,00 em até 00x", disabled=True)
        st.text_input("1 Intercalada:", value="Potencial de: R$ 0,00", disabled=True)
        st.text_input("2 Intercalada:", value="Potencial de: R$ 0,00", disabled=True)
        st.text_input("3 Intercalada:", value="Potencial de: R$ 0,00", disabled=True)
        st.text_input("4 Intercalada:", value="Potencial de: R$ 0,00", disabled=True)
        st.text_input("5 Intercalada:", value="Potencial de: R$ 0,00", disabled=True)
        st.text_input("Parcela Única:", value="Parcela chave:", disabled=True)
        desc_condicionado = st.toggle("Desconto Condicionado?")
    with c1:
        quantidade_mensais = st.text_input("Qtd. mensais", value="0")
    with c2:
        valor_mensais = st.text_input("Valor Parcela", value="0.00")
        
    with c3:
        valor_parc_total = st.text_input("Valor Total ", value=real_br_money_mask(float(valor_mensais)*int(quantidade_mensais)), disabled=True)
        inter1 = st.text_input("Valor Inter1", value="0.00")
        inter2 = st.text_input("Valor Inter2", value="0.00")
        inter3 = st.text_input("Valor Inter3", value="0.00")
        inter4 = st.text_input("Valor Inter4", value="0.00")
        inter5 = st.text_input("Valor Inter5", value="0.00")
        ch = st.text_input("Valor chave", value="0.00")
        if desc_condicionado == True:
            var = False
        else:
            var = True
        desc_cond = st.text_input("Valor Desc.", value="0.00", disabled=var)
    
    with c4:
        st.text_input("Data mensais", value="2024-01-01")
        st.text_input("Data Inter1", value="2024-01-01")
        st.text_input("Data Inter2", value="2024-01-01")
        st.text_input("Data Inter3", value="2024-01-01")
        st.text_input("Data Inter4", value="2024-01-01")
        st.text_input("Data Inter5", value="2024-01-01")


with pilar4.container(border=True):
    st.html("""
            <style>
                .custom-banner5 {
                    color: white;
                    background-color: #006400;
                    border-radius: 10px;
                    width: 100%;
                    padding: 5px;
                    margin: 5px auto;
                    text-align: center;
                    font-size: 14px;
                    font-weight: bold;
                }

                /* Media query para telas médias */
                @media (min-width: 768px) {
                    .custom-banner {
                        width: 100%;
                    }
                }

                /* Media query para telas grandes */
                @media (min-width: 1024px) {
                    .custom-banner {
                        width: 100%;
                    }
                }
            </style>

            <div class="custom-banner5">
                POUPANÇA - LONGO PRAZO
            </div>
        """)
    c0, c1, c2, c3, c4 = st.columns([2, 1,1,1,1])
    with c0:
        st.text_input("Parc Pós:", value="Máx de R$ 0,00 em até 00x", disabled=True)

    with c1:
        quantidade_mensais_pos = st.text_input("Qtd. mensais pós", value="0")
    with c2:
        valor_mensais_pos = st.text_input("Valor Parcela pós", value="0.00")
    with c3:
        valor_parc_total_pos = st.text_input("Valor Total", value=real_br_money_mask(float(valor_mensais_pos)*int(quantidade_mensais_pos)), disabled=True)
    with c4:
        st.text_input("Data mensais pós", value="2024-01-01")


st.html("""
        <style>
            .custom-banner3 {
                color: white;
                background-color: #008080;
                border-radius: 10px;
                width: 100%;
                padding: 5px;
                margin: 5px auto;
                text-align: center;
                font-size: 14px;
                font-weight: bold;
            }

            /* Media query para telas médias */
            @media (min-width: 768px) {
                .custom-banner {
                    width: 100%;
                }
            }

            /* Media query para telas grandes */
            @media (min-width: 1024px) {
                .custom-banner {
                    width: 100%;
                }
            }
        </style>

        <div class="custom-banner3">
            ANÁLISE PLANO DE PAGAMENTO:
        </div>
    """)

espaco1, espaco2, espaco3 = st.columns([5, 5, 5])

with espaco1.container(border=True):  
    st.html("""
            <style>
                .custom-banner6 {
                    color: white;
                    background-color: #696969;
                    border-radius: 10px;
                    width: 100%;
                    padding: 5px;
                    margin: 5px auto;
                    text-align: center;
                    font-size: 14px;
                    font-weight: bold;
                }

                /* Media query para telas médias */
                @media (min-width: 768px) {
                    .custom-banner {
                        width: 100%;
                    }
                }

                /* Media query para telas grandes */
                @media (min-width: 1024px) {
                    .custom-banner {
                        width: 100%;
                    }
                }
            </style>

            <div class="custom-banner6">
                LIBERAÇÕES:
            </div>
        """)
   
    st.warning("STATUS: Mensal pós superior ao permitido")
    st.success("GARANTIDO: OK")
    st.error("PÓS: Atenção! Alçada Comitê")




with espaco2.container(border=True):  
    st.html("""
            <style>
                .custom-banner6 {
                    color: white;
                    background-color: #696969;
                    border-radius: 10px;
                    width: 100%;
                    padding: 5px;
                    margin: 5px auto;
                    text-align: center;
                    font-size: 14px;
                    font-weight: bold;
                }

                /* Media query para telas médias */
                @media (min-width: 768px) {
                    .custom-banner {
                        width: 100%;
                    }
                }

                /* Media query para telas grandes */
                @media (min-width: 1024px) {
                    .custom-banner {
                        width: 100%;
                    }
                }
            </style>

            <div class="custom-banner6">
                CONFERÊNCIA DE TABELA:
            </div>
        """)
    dados = {"Tabela": "202.000,00", "VGV Bruto":"202.000,00", "VGV Líquido":"198.000,00", "Dif (R$)":"0,00"}
    data = pd.DataFrame([dados])
    data.index.name = "Resultado"
    st.html("""
    <style>
        .custom-table {
            width: 100%;
            border-collapse: collapse;
            margin: 5px 0;
        }
        .custom-table th, .custom-table td {
            border: 1px solid #ddd;
            padding: 5px;
            text-align: center;
            
        }
        .custom-table th {
            background-color: #FF6347;
            color: white;
          
        }
    </style>

    <table class="custom-table">
        <tr>
            <th>Tabela</th>
            <th>VGV Bruto</th>
            <th>VGV Líquido</th>
            <th>Dif (R$)</th>
        </tr>
        <tr>
            <td>202.000,00</td>
            <td>202.000,00</td>
            <td>198.000,00</td>
            <td>0,00</td>
        </tr>
    </table>
""")
    st.text("")
    st.html("""
            <style>
                .custom-banner7 {
                    color: white;
                    background-color: #DC143C;
                    border-radius: 10px;
                    width: 100%;
                    padding: 5px;
                    margin: 5px auto;
                    text-align: center;
                    font-size: 14px;
                    font-weight: bold;
                }

                /* Media query para telas médias */
                @media (min-width: 768px) {
                    .custom-banner {
                        width: 100%;
                    }
                }

                /* Media query para telas grandes */
                @media (min-width: 1024px) {
                    .custom-banner {
                        width: 100%;
                    }
                }
            </style>

            <div class="custom-banner7">
                REVISAR
            </div>
            <center>
                <h6>STATUS GERAL</h6>
            </center>
        """)

with espaco3.container(border=True):  
    st.html("""
            <style>
                .custom-banner8 {
                    color: white;
                    background-color: #696969;
                    border-radius: 10px;
                    width: 100%;
                    padding: 5px;
                    margin: 5px auto;
                    text-align: center;
                    font-size: 14px;
                    font-weight: bold;
                }

                /* Media query para telas médias */
                @media (min-width: 768px) {
                    .custom-banner {
                        width: 100%;
                    }
                }

                /* Media query para telas grandes */
                @media (min-width: 1024px) {
                    .custom-banner {
                        width: 100%;
                    }
                }
            </style>

            <div class="custom-banner8">
               RESUMO DO PLANO:
            </div>
        """)
    st.html("""
    <style>
        .custom-table {
            width: 100%;
            border-collapse: collapse;
            margin: 3px 0;
        }
        .custom-table th, .custom-table td {
            border: 0.5px solid #ddd;
            padding: 5px;
            text-align: center;
            
        }
        .custom-table th {
            background-color: #FF6347;
            color: white;
          
        }
    </style>

    <table class="custom-table">
        <tr>
            <th>Garantido Total</th>
            <th>Poup-Curto Prazo</th>
            <th>Poup-Longo Prazo</th>
        </tr>
        <tr>
            <td>85%</td>
            <td>10%</td>
            <td>5%</td>
        </tr>
        <tr>
            <td>202.000,00</td>
            <td>202.000,00</td>
            <td>198.000,00</td>
        </tr>
        <tr>
            <td>85%</td>
            <td>10%</td>
            <td>5%</td>
        </tr>
    </table>
""")
    st.text("")
    st.text("")
