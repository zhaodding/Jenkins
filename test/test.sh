#!/bin/bash
#kubectl get ns|grep dev
ns=`kubectl get ns |grep dev|awk '{print $1}' |tail -n 1`
num=`kubectl get pods -n $ns |wc -l`
# kubectl get pods -n $ns|awk '{print $1}'|sed -n 2,${num}'p'
deploy=`kubectl get deploy -n $ns|awk '{print $1}'|sed -n 2,${num}'p'`
# pods=kubectl get pods -n $ns|awk '{print $1}'|sed -n 2,${num}'p'
memTotal=`kubectl -n $ns get deployment $deploy -o yaml |grep memory|tail -n 1`
deploy
memTotal


