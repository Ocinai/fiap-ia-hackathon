import argparse
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import transforms
from torch.utils.data import DataLoader
from src.supervised_model.model import SimpleCNN, save_model, ImageDataset

def main():
    parser = argparse.ArgumentParser(description='Train a simple CNN model on a dataset of images.')
    parser.add_argument('--data_dir', type=str, default='dataset/', help='Path to the dataset directory.')
    parser.add_argument('--model_path', type=str, default='model/supervised_model.pth', help='Path to save the trained model.')
    parser.add_argument('--num_epochs', type=int, default=10, help='Number of epochs to train for.')
    parser.add_argument('--batch_size', type=int, default=32, help='Batch size for training.')
    parser.add_argument('--learning_rate', type=float, default=0.001, help='Learning rate for the optimizer.')
    parser.add_argument('--num_classes', type=int, default=10, help='Number of classes in the dataset.')
    args = parser.parse_args()

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    train_dataset = ImageDataset(root_dir=args.data_dir, transform=transform)
    train_loader = DataLoader(dataset=train_dataset, batch_size=args.batch_size, shuffle=True)

    model = SimpleCNN(num_classes=args.num_classes)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=args.learning_rate)

    print("Starting training...")
    for epoch in range(args.num_epochs):
        for i, (images, labels) in enumerate(train_loader):
            outputs = model(images)
            loss = criterion(outputs, labels)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            if (i+1) % 10 == 0:
                print(f'Epoch [{epoch+1}/{args.num_epochs}], Step [{i+1}/{len(train_loader)}], Loss: {loss.item():.4f}')
    
    print("Training finished.")

    save_model(model, args.model_path)
    print(f"Model saved to {args.model_path}")

if __name__ == '__main__':
    main()
