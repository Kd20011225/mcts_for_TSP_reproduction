import torch
import torch.nn.functional as F


def create_heatmap_matrix(batch_coords, tau, device="cuda:0"):
    batch_coords = torch.tensor(batch_coords, device=device).float()

    coord_diff = batch_coords[:, :, None, :] - batch_coords[:, None, :, :]

    distance_matrix = torch.sqrt(torch.sum(coord_diff ** 2, dim=-1))

    eye = torch.eye(distance_matrix.size(1), device=device).unsqueeze(0)
    distance_matrix = torch.where(
    eye == 1,
    torch.tensor(float('inf'), dtype=torch.float, device=device),
    distance_matrix
    )

    heatmap = F.softmax(-distance_matrix / tau, dim=2)

    return heatmap.cpu().numpy()