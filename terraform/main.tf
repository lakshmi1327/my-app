provider "aws" {
  region = "us-west-2"
}

resource "aws_eks_cluster" "my-cluster" {
  name     = "my-cluster"
  role_arn = aws_iam_role.eks-cluster.arn

  vpc_config {
    subnet_ids = aws_subnet.public.*.id
  }
}
