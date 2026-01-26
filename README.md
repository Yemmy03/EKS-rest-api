### Spining up my first k8s Cluster and why you should not use a free tier account for this
---

# Steps & Error Resolution Walkthrough: Pushing a Rest API Container to Kubernetes (EKS)

## **Summary**

Deploy a containerized REST API to AWS EKS using yaml manifests.

---

# 1. **Repository & Kubernetes Manifests**

I started with a repo containing:  

```
app/
Dockerfile
k8s/
  deployment.yaml
  service.yaml
```

The Kubernetes manifests were already created and stored on GitHub.

---

# 2. **Pulling the YAML Files to Local**

I cloned or pulled the repository from GitHub to my local machine:

```bash
git clone <repo-url>
cd eks-rest-api
code .
```

---

# 3. **Initial Kubernetes Apply**

I tried:

```bash
kubectl apply -f deployment.yaml
```

But got:

```
error: the path "deployment.yaml" does not exist
```

### Why?

Because the YAML file is inside the `k8s/` directory, not the root.

So I tried the below command to fetch the exact dir path:

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

Or one can also try the below to apply the whole folder:

```bash
kubectl apply -f k8s/
```

---

# 4. **Pods Stuck in Pending**

After deploying the Deployment, the pods were stuck in:

```
Pending
```

I checked pod status:

```bash
kubectl get pods -n default
```

And described the pod:

```bash
kubectl describe pod <pod-name>
```

The error was:

```
0/1 nodes are available: 1 Too many pods
```

### Meaning:
```
The node had reached its maximum pod capacity and could not accept new pods.
So I need to quickly chip in the fact that I used a free tier account (aws builder) for this project.
It gave me alot of restrictions tho, I could only use the t3.micro instance type or less which was still not enough.
A great option was to create another nodegroup and spin another node on the cluster but the account type didn't allow for it.
I explained in more technical terms in the subsequent sections.
```
---

# 5. **Cluster Capacity Issues**

I identified the root cause with the cluster via logs and discovered:

* Only Node that exists is **maxed out**
* EKS default limits on pods per node were reached

---

# 6. **Free Tier Limitation**

Another issue I lat tried using `t3.micro` and `t3.small`.

You confirmed:

### Free Tier supports only:

* **t3.micro (or t2.micro)**

### Conclusion:

**My application is not feasible on free tier EKS** due to:

* Limited CPU/RAM
* Low pod capacity
* Limited nodes
---

## Wins and Questions:
```
1. I had no issue configuring the cluster.
```
<img width="1431" height="417" alt="image" src="https://github.com/user-attachments/assets/0f62be6f-e438-41bc-aabc-78d2123568d8" />

---

```
2. I had no issue configuring vpc, subnets and SG (security groups), I had read alot in theory about them and it just felt like putting puzzles together.
```
<img width="1400" height="371" alt="image" src="https://github.com/user-attachments/assets/2a9efdd0-29e5-4b87-b76f-744d9c72e8ec" />

---

```
3. I had this question while dealing with networking configuration...
When accessing the EKS API server, why is it recommended to make the server endpoint private and use a bastion or VPN, rather than keeping it public and restricting access via CIDR whitelisting of my IP? 
```











