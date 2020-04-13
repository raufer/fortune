### GCP

Setup

```bash
gcloud auth login
```

```bash
gcloud config set project weighty-purpose-273914
```

Create a GCP `Project Owner` Service Account

```bash
PROJECT_ID=weighty-purpose-273914
NAME=ryze-admin
gcloud iam service-accounts create $NAME
gcloud projects add-iam-policy-binding $PROJECT_ID --member "serviceAccount:$NAME@$PROJECT_ID.iam.gserviceaccount.com" --role "roles/owner"
gcloud iam service-accounts keys create auth/credentials.json --iam-account $NAME@$PROJECT_ID.iam.gserviceaccount.com
```
