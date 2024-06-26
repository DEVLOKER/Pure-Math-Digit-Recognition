import os
import matplotlib.pyplot as plt

class TrainingHistory(object):

    TRAINING_HISTORY= os.path.join("training", "training_history.jpg")

    def __init__(self):
        self.init()

    def init(self, total_epochs=None):
        self.total_epochs = total_epochs
        self.epochs = []
        self.training_accuracy = []
        self.training_loss = []
        self.validation_accuracy = []
        self.validation_loss = []

    def append_history(self, epoch, training_accuracy, training_loss, validation_accuracy, validation_loss):
        self.epochs.append(epoch)
        self.training_accuracy.append(training_accuracy)
        self.training_loss.append(training_loss)
        self.validation_accuracy.append(validation_accuracy)
        self.validation_loss.append(validation_loss)
        text, _, _, _ , _, _ = self.get_last_history_epoch()
        print(text)
        return text, _, _, _ , _, _ 

    def set_total_epochs(self, total_epochs):
        self.total_epochs = total_epochs

    def get_total_epochs(self):
        return self.total_epochs
    
    def get_epochs(self):
        return self.epochs
    
    def get_training_accuracy(self):
        return self.training_accuracy
    
    def get_training_loss(self):
        return self.training_loss
    
    def get_validation_accuracy(self):
        return self.validation_accuracy
    
    def get_validation_loss(self):
        return self.validation_loss
    
    def get_history(self):
        return self.epochs, self.training_accuracy, self.training_loss, self.validation_accuracy, self.validation_loss
    

    def get_history_by_epoch(self, index):
        try:
            epoch = self.epochs[index]
            training_accuracy = self.training_accuracy[index]
            training_loss = self.training_loss[index]
            validation_accuracy = self.validation_accuracy[index]
            validation_loss = self.validation_loss[index]
            text = self.get_current_history_string(epoch, training_accuracy, training_loss, validation_accuracy, validation_loss)
            return text, epoch, training_accuracy, training_loss, validation_accuracy, validation_loss
        except Exception:
            return "", 0, 0, 0, 0, 0

        
    
    def get_last_history_epoch(self):
        return self.get_history_by_epoch(-1)
    
    def get_current_history_string(self, epoch, training_accuracy, training_loss, validation_accuracy, validation_loss):
        total_epochs = self.total_epochs if self.total_epochs != None else epoch
        text = f"""Iteration: {epoch} / {max(epoch, total_epochs)}\nTraining Accuracy: {training_accuracy:.3%} \t Training Loss: {training_loss:.3f}\nValidation Accuracy: {validation_accuracy:.3%} \t Validation Loss: {validation_loss:.3f}\n"""
        return text

    def show_evaluation(self, filename=TRAINING_HISTORY):
        # Create a single figure with two subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
        fig.suptitle("Accuracy vs Loss", fontsize=14)

        # Plot training & validation accuracy values
        ax1.plot(self.training_accuracy)
        ax1.plot(self.validation_accuracy)
        ax1.set_title('Model accuracy')
        ax1.set_ylabel('Accuracy')
        ax1.set_xlabel('Epoch')
        ax1.legend(['Training', 'Validation'], loc='upper left')
        
        # Plot training & validation loss values
        ax2.plot(self.training_loss)
        ax2.plot(self.validation_loss)
        ax2.set_title('Model loss')
        ax2.set_ylabel('Loss')
        ax2.set_xlabel('Epoch')
        ax2.legend(['Training', 'Validation'], loc='upper left')
        
        plt.savefig(filename)
        plt.show()