# create_notebook.py
import json
import os

# Create 'notebooks' directory if it doesn't exist
os.makedirs("notebooks", exist_ok=True)

# Define the exact JSON structure of a valid Jupyter Notebook
notebook_data = {
    "cells":
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs":,
            "source":
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs":,
            "source":
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs":,
            "source":
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs":,
            "source":
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs":,
            "source":
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs":,
            "source":
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs":,
            "source":\n",
                "corr_matrix = df[corr_cols].corr()\n",
                "\n",
                "sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)\n",
                "plt.title('Pearson Correlation Heatmap of Surveillance Features')\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source":
        }
    ],
    "metadata": {
        "language_info": {
            "name": "python"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 2
}

# Write the JSON data to notebooks/analysis.ipynb
filepath = os.path.join("notebooks", "analysis.ipynb")
with open(filepath, "w", encoding="utf-8") as f:
    json.dump(notebook_data, f, indent=2)

print("🎉 Success! 'notebooks/analysis.ipynb' has been automatically created with perfect formatting!")