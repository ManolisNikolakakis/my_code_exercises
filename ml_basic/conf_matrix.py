import numpy as np

def confusion_matrix(y_true, y_pred):
    classes = np.unique(np.concatenate([y_true, y_pred]))
    n_classes = len(classes)
    matrix = np.zeros((n_classes, n_classes), dtype=int)
    
    for true, pred in zip(y_true, y_pred):
        matrix[true, pred] += 1
    
    return matrix


if __name__ == "__main__":
    y_true = np.array([0, 1, 0, 1, 0, 1, 0, 1])
    y_pred = np.array([0, 1, 0, 0, 0, 1, 1, 1])
    
    cm = confusion_matrix(y_true, y_pred)
    print("Confusion Matrix:")
    print(cm)
    print("\nFormat:")
    print("       Pred 0  Pred 1")
    print("True 0   TN      FP")
    print("True 1   FN      TP")