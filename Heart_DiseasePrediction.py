{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Heart_DiseasePrediction.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "toc_visible": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "Importing the dependencies"
      ],
      "metadata": {
        "id": "Ah0tbPA2Ks2h"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "QQPgXdhXJ6y9"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.linear_model import LogisticRegression\n",
        "from sklearn.metrics import accuracy_score"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Data collection and processing"
      ],
      "metadata": {
        "id": "K9VM91VQLgLG"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#loading the csv data to a Pandas DtaFrame\n",
        "heart_data = pd.read_csv('/content/heart_disease_data.csv')"
      ],
      "metadata": {
        "id": "4Ng8ghQpLd7A"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# print first 5 rows of the dataset\n",
        "heart_data.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "tZArx3OqL5S_",
        "outputId": "51624fd7-3d89-4934-ff29-2833acd64c7b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   age  sex  cp  trestbps  chol  fbs  restecg  thalach  exang  oldpeak  slope  \\\n",
              "0   63    1   3       145   233    1        0      150      0      2.3      0   \n",
              "1   37    1   2       130   250    0        1      187      0      3.5      0   \n",
              "2   41    0   1       130   204    0        0      172      0      1.4      2   \n",
              "3   56    1   1       120   236    0        1      178      0      0.8      2   \n",
              "4   57    0   0       120   354    0        1      163      1      0.6      2   \n",
              "\n",
              "   ca  thal  target  \n",
              "0   0     1       1  \n",
              "1   0     2       1  \n",
              "2   0     2       1  \n",
              "3   0     2       1  \n",
              "4   0     2       1  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-e58b2e61-a4a0-4c3b-98a5-fb99de5dd1bd\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>age</th>\n",
              "      <th>sex</th>\n",
              "      <th>cp</th>\n",
              "      <th>trestbps</th>\n",
              "      <th>chol</th>\n",
              "      <th>fbs</th>\n",
              "      <th>restecg</th>\n",
              "      <th>thalach</th>\n",
              "      <th>exang</th>\n",
              "      <th>oldpeak</th>\n",
              "      <th>slope</th>\n",
              "      <th>ca</th>\n",
              "      <th>thal</th>\n",
              "      <th>target</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>63</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>145</td>\n",
              "      <td>233</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>150</td>\n",
              "      <td>0</td>\n",
              "      <td>2.3</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>37</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>130</td>\n",
              "      <td>250</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>187</td>\n",
              "      <td>0</td>\n",
              "      <td>3.5</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>41</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>130</td>\n",
              "      <td>204</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>172</td>\n",
              "      <td>0</td>\n",
              "      <td>1.4</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>56</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>120</td>\n",
              "      <td>236</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>178</td>\n",
              "      <td>0</td>\n",
              "      <td>0.8</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>57</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>120</td>\n",
              "      <td>354</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>163</td>\n",
              "      <td>1</td>\n",
              "      <td>0.6</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-e58b2e61-a4a0-4c3b-98a5-fb99de5dd1bd')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-e58b2e61-a4a0-4c3b-98a5-fb99de5dd1bd button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-e58b2e61-a4a0-4c3b-98a5-fb99de5dd1bd');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# print last 5 rows of the dataset\n",
        "heart_data.tail()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 250
        },
        "id": "gSbclwuYMEaW",
        "outputId": "762f4e55-7875-408d-8039-c73016639492"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "     age  sex  cp  trestbps  chol  fbs  restecg  thalach  exang  oldpeak  \\\n",
              "298   57    0   0       140   241    0        1      123      1      0.2   \n",
              "299   45    1   3       110   264    0        1      132      0      1.2   \n",
              "300   68    1   0       144   193    1        1      141      0      3.4   \n",
              "301   57    1   0       130   131    0        1      115      1      1.2   \n",
              "302   57    0   1       130   236    0        0      174      0      0.0   \n",
              "\n",
              "     slope  ca  thal  target  \n",
              "298      1   0     3       0  \n",
              "299      1   0     3       0  \n",
              "300      1   2     3       0  \n",
              "301      1   1     3       0  \n",
              "302      1   1     2       0  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-b3c015a0-983c-422d-b44f-85af973e9115\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>age</th>\n",
              "      <th>sex</th>\n",
              "      <th>cp</th>\n",
              "      <th>trestbps</th>\n",
              "      <th>chol</th>\n",
              "      <th>fbs</th>\n",
              "      <th>restecg</th>\n",
              "      <th>thalach</th>\n",
              "      <th>exang</th>\n",
              "      <th>oldpeak</th>\n",
              "      <th>slope</th>\n",
              "      <th>ca</th>\n",
              "      <th>thal</th>\n",
              "      <th>target</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>298</th>\n",
              "      <td>57</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>140</td>\n",
              "      <td>241</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>123</td>\n",
              "      <td>1</td>\n",
              "      <td>0.2</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>299</th>\n",
              "      <td>45</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>110</td>\n",
              "      <td>264</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>132</td>\n",
              "      <td>0</td>\n",
              "      <td>1.2</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>300</th>\n",
              "      <td>68</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>144</td>\n",
              "      <td>193</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>141</td>\n",
              "      <td>0</td>\n",
              "      <td>3.4</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>3</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>301</th>\n",
              "      <td>57</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>130</td>\n",
              "      <td>131</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>115</td>\n",
              "      <td>1</td>\n",
              "      <td>1.2</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>302</th>\n",
              "      <td>57</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>130</td>\n",
              "      <td>236</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>174</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-b3c015a0-983c-422d-b44f-85af973e9115')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-b3c015a0-983c-422d-b44f-85af973e9115 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-b3c015a0-983c-422d-b44f-85af973e9115');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# number of rows and column of the dataset\n",
        "heart_data.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "R0NJCWouMR6m",
        "outputId": "26587760-901c-47bb-f32b-8aab16c6c118"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(303, 14)"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# getting some info about the data\n",
        "heart_data.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OabYyy6HMajN",
        "outputId": "c30e95a3-4aef-40c8-aafd-1e7b04fb77bd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 303 entries, 0 to 302\n",
            "Data columns (total 14 columns):\n",
            " #   Column    Non-Null Count  Dtype  \n",
            "---  ------    --------------  -----  \n",
            " 0   age       303 non-null    int64  \n",
            " 1   sex       303 non-null    int64  \n",
            " 2   cp        303 non-null    int64  \n",
            " 3   trestbps  303 non-null    int64  \n",
            " 4   chol      303 non-null    int64  \n",
            " 5   fbs       303 non-null    int64  \n",
            " 6   restecg   303 non-null    int64  \n",
            " 7   thalach   303 non-null    int64  \n",
            " 8   exang     303 non-null    int64  \n",
            " 9   oldpeak   303 non-null    float64\n",
            " 10  slope     303 non-null    int64  \n",
            " 11  ca        303 non-null    int64  \n",
            " 12  thal      303 non-null    int64  \n",
            " 13  target    303 non-null    int64  \n",
            "dtypes: float64(1), int64(13)\n",
            "memory usage: 33.3 KB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# checking for missing values \n",
        "heart_data.isnull().sum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "I-Sv4GjFMnxV",
        "outputId": "aef072b2-9b19-4f9e-c5f5-0c0d7b8d2a8b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "age         0\n",
              "sex         0\n",
              "cp          0\n",
              "trestbps    0\n",
              "chol        0\n",
              "fbs         0\n",
              "restecg     0\n",
              "thalach     0\n",
              "exang       0\n",
              "oldpeak     0\n",
              "slope       0\n",
              "ca          0\n",
              "thal        0\n",
              "target      0\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# statistical measures about the data\n",
        "heart_data.describe()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 364
        },
        "id": "L5CwQLwdM1zE",
        "outputId": "f7385531-4c37-4914-fe39-90cfc5b7c5cb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "              age         sex          cp    trestbps        chol         fbs  \\\n",
              "count  303.000000  303.000000  303.000000  303.000000  303.000000  303.000000   \n",
              "mean    54.366337    0.683168    0.966997  131.623762  246.264026    0.148515   \n",
              "std      9.082101    0.466011    1.032052   17.538143   51.830751    0.356198   \n",
              "min     29.000000    0.000000    0.000000   94.000000  126.000000    0.000000   \n",
              "25%     47.500000    0.000000    0.000000  120.000000  211.000000    0.000000   \n",
              "50%     55.000000    1.000000    1.000000  130.000000  240.000000    0.000000   \n",
              "75%     61.000000    1.000000    2.000000  140.000000  274.500000    0.000000   \n",
              "max     77.000000    1.000000    3.000000  200.000000  564.000000    1.000000   \n",
              "\n",
              "          restecg     thalach       exang     oldpeak       slope          ca  \\\n",
              "count  303.000000  303.000000  303.000000  303.000000  303.000000  303.000000   \n",
              "mean     0.528053  149.646865    0.326733    1.039604    1.399340    0.729373   \n",
              "std      0.525860   22.905161    0.469794    1.161075    0.616226    1.022606   \n",
              "min      0.000000   71.000000    0.000000    0.000000    0.000000    0.000000   \n",
              "25%      0.000000  133.500000    0.000000    0.000000    1.000000    0.000000   \n",
              "50%      1.000000  153.000000    0.000000    0.800000    1.000000    0.000000   \n",
              "75%      1.000000  166.000000    1.000000    1.600000    2.000000    1.000000   \n",
              "max      2.000000  202.000000    1.000000    6.200000    2.000000    4.000000   \n",
              "\n",
              "             thal      target  \n",
              "count  303.000000  303.000000  \n",
              "mean     2.313531    0.544554  \n",
              "std      0.612277    0.498835  \n",
              "min      0.000000    0.000000  \n",
              "25%      2.000000    0.000000  \n",
              "50%      2.000000    1.000000  \n",
              "75%      3.000000    1.000000  \n",
              "max      3.000000    1.000000  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-cc5e67e2-fa6a-4cd3-9da7-efb8921eda59\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>age</th>\n",
              "      <th>sex</th>\n",
              "      <th>cp</th>\n",
              "      <th>trestbps</th>\n",
              "      <th>chol</th>\n",
              "      <th>fbs</th>\n",
              "      <th>restecg</th>\n",
              "      <th>thalach</th>\n",
              "      <th>exang</th>\n",
              "      <th>oldpeak</th>\n",
              "      <th>slope</th>\n",
              "      <th>ca</th>\n",
              "      <th>thal</th>\n",
              "      <th>target</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>303.000000</td>\n",
              "      <td>303.000000</td>\n",
              "      <td>303.000000</td>\n",
              "      <td>303.000000</td>\n",
              "      <td>303.000000</td>\n",
              "      <td>303.000000</td>\n",
              "      <td>303.000000</td>\n",
              "      <td>303.000000</td>\n",
              "      <td>303.000000</td>\n",
              "      <td>303.000000</td>\n",
              "      <td>303.000000</td>\n",
              "      <td>303.000000</td>\n",
              "      <td>303.000000</td>\n",
              "      <td>303.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>54.366337</td>\n",
              "      <td>0.683168</td>\n",
              "      <td>0.966997</td>\n",
              "      <td>131.623762</td>\n",
              "      <td>246.264026</td>\n",
              "      <td>0.148515</td>\n",
              "      <td>0.528053</td>\n",
              "      <td>149.646865</td>\n",
              "      <td>0.326733</td>\n",
              "      <td>1.039604</td>\n",
              "      <td>1.399340</td>\n",
              "      <td>0.729373</td>\n",
              "      <td>2.313531</td>\n",
              "      <td>0.544554</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>9.082101</td>\n",
              "      <td>0.466011</td>\n",
              "      <td>1.032052</td>\n",
              "      <td>17.538143</td>\n",
              "      <td>51.830751</td>\n",
              "      <td>0.356198</td>\n",
              "      <td>0.525860</td>\n",
              "      <td>22.905161</td>\n",
              "      <td>0.469794</td>\n",
              "      <td>1.161075</td>\n",
              "      <td>0.616226</td>\n",
              "      <td>1.022606</td>\n",
              "      <td>0.612277</td>\n",
              "      <td>0.498835</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>29.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>94.000000</td>\n",
              "      <td>126.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>71.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>47.500000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>120.000000</td>\n",
              "      <td>211.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>133.500000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>55.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>130.000000</td>\n",
              "      <td>240.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>153.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.800000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>61.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>140.000000</td>\n",
              "      <td>274.500000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>166.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.600000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>77.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>200.000000</td>\n",
              "      <td>564.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>202.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>6.200000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-cc5e67e2-fa6a-4cd3-9da7-efb8921eda59')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-cc5e67e2-fa6a-4cd3-9da7-efb8921eda59 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-cc5e67e2-fa6a-4cd3-9da7-efb8921eda59');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# checking the distributationof Target Variable\n",
        "heart_data['target'].value_counts()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "N4d0U6cUNg3e",
        "outputId": "f541dc95-5964-4cee-a54c-6ef9abcb8673"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1    165\n",
              "0    138\n",
              "Name: target, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "1 --> represent Defective Heart\n",
        "0 --> represent Healthy Heart"
      ],
      "metadata": {
        "id": "cGfDd9RiOJZe"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Splitting the Features and Targer"
      ],
      "metadata": {
        "id": "dd1sv_NsOoMb"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "X = heart_data.drop(columns='target',axis=1)\n",
        "Y=  heart_data['target']"
      ],
      "metadata": {
        "id": "IqZTH7n_OW26"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(X)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dEitdsfIPCoU",
        "outputId": "fb593a07-00e8-41eb-e654-081766a58ce8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "     age  sex  cp  trestbps  chol  fbs  restecg  thalach  exang  oldpeak  \\\n",
            "0     63    1   3       145   233    1        0      150      0      2.3   \n",
            "1     37    1   2       130   250    0        1      187      0      3.5   \n",
            "2     41    0   1       130   204    0        0      172      0      1.4   \n",
            "3     56    1   1       120   236    0        1      178      0      0.8   \n",
            "4     57    0   0       120   354    0        1      163      1      0.6   \n",
            "..   ...  ...  ..       ...   ...  ...      ...      ...    ...      ...   \n",
            "298   57    0   0       140   241    0        1      123      1      0.2   \n",
            "299   45    1   3       110   264    0        1      132      0      1.2   \n",
            "300   68    1   0       144   193    1        1      141      0      3.4   \n",
            "301   57    1   0       130   131    0        1      115      1      1.2   \n",
            "302   57    0   1       130   236    0        0      174      0      0.0   \n",
            "\n",
            "     slope  ca  thal  \n",
            "0        0   0     1  \n",
            "1        0   0     2  \n",
            "2        2   0     2  \n",
            "3        2   0     2  \n",
            "4        2   0     2  \n",
            "..     ...  ..   ...  \n",
            "298      1   0     3  \n",
            "299      1   0     3  \n",
            "300      1   2     3  \n",
            "301      1   1     3  \n",
            "302      1   1     2  \n",
            "\n",
            "[303 rows x 13 columns]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(Y)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zdtG6La-PLN9",
        "outputId": "052ab13d-d634-49af-961c-c9263f7c47e8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0      1\n",
            "1      1\n",
            "2      1\n",
            "3      1\n",
            "4      1\n",
            "      ..\n",
            "298    0\n",
            "299    0\n",
            "300    0\n",
            "301    0\n",
            "302    0\n",
            "Name: target, Length: 303, dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Spliittig the data into Training Data and Test data"
      ],
      "metadata": {
        "id": "EGZ9_DUaPUgt"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "x_train, x_test, y_train,y_test = train_test_split(X,Y,test_size=0.2,stratify=Y,random_state=2)"
      ],
      "metadata": {
        "id": "v82cJzatPQG8"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(X.shape, x_train.shape,x_test.shape)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QFWnN_6_P_9e",
        "outputId": "c6596cfd-be4b-4ef3-f115-81290b4b6bd1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(303, 13) (242, 13) (61, 13)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Model Training "
      ],
      "metadata": {
        "id": "wom74fhnQOkM"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Logistinc Regression Model"
      ],
      "metadata": {
        "id": "g58aV0MOQSkz"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "model = LogisticRegression()"
      ],
      "metadata": {
        "id": "Gymite7nQNo0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# training the logistic Regression model\n",
        "model.fit(x_train,y_train)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fk3cBU5MQf2S",
        "outputId": "cfeed05f-bcb5-4f4c-dfc6-1fb30cbeab5d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/sklearn/linear_model/_logistic.py:818: ConvergenceWarning: lbfgs failed to converge (status=1):\n",
            "STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.\n",
            "\n",
            "Increase the number of iterations (max_iter) or scale the data as shown in:\n",
            "    https://scikit-learn.org/stable/modules/preprocessing.html\n",
            "Please also refer to the documentation for alternative solver options:\n",
            "    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression\n",
            "  extra_warning_msg=_LOGISTIC_SOLVER_CONVERGENCE_MSG,\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "LogisticRegression()"
            ]
          },
          "metadata": {},
          "execution_count": 22
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Model Evaluation"
      ],
      "metadata": {
        "id": "HdPHtbntRA88"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# accuracy on trining data\n",
        "x_train_prediction = model.predict(x_train)\n",
        "training_data_accuracy = accuracy_score(x_train_prediction, y_train)"
      ],
      "metadata": {
        "id": "XoRoxe8vQ8N8"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print('Accuracy on training data: ',training_data_accuracy)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "619fxBWHRmYe",
        "outputId": "98ef1d55-7d0f-48aa-fedd-c64947d2f363"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Accuracy on training data:  0.8512396694214877\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# accuracy on test data\n",
        "x_test_prediction = model.predict(x_test)\n",
        "test_data_accuracy = accuracy_score(x_test_prediction, y_test)"
      ],
      "metadata": {
        "id": "YEDy48FRRw-1"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print('Accuracy on Test Data: ',test_data_accuracy)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iIe3-3FjSMg0",
        "outputId": "dae06d85-8644-4665-cfc8-b5282e19eda6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Accuracy on Test Data:  0.819672131147541\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Buildng a Preediction System"
      ],
      "metadata": {
        "id": "plOj_DzWSkFH"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "input_data= (51,0,0,130,305,0,1,142,1,1.2,1,0,3)\n",
        "\n",
        "#Change The Input Data to numpy Array\n",
        "input_data_as_numpy_array = np.asarray(input_data)\n",
        "\n",
        "# reshape the numpy array as we are predicting for only on instance\n",
        "input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)\n",
        "\n",
        "prediction = model.predict(input_data_reshaped)\n",
        "\n",
        "print(prediction)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "U8JnhVuuSd96",
        "outputId": "d3fa523f-d3da-4d73-9370-cfd9f825b07c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[0]\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/sklearn/base.py:451: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names\n",
            "  \"X does not have valid feature names, but\"\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "if(prediction[0]==0):\n",
        " print('The person has no heart deasease')\n",
        "else:\n",
        " print('The person has a Heart disease')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "U_DP80asUvSl",
        "outputId": "a1d2fc95-db29-47cd-da8a-b3721be19360"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The person has no heart deasease\n"
          ]
        }
      ]
    }
  ]
}