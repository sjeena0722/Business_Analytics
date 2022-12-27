from __future__ import print_function, absolute_import

__all__ = ['accuracy']

def accuracy(output, target, topk=(1,)):
    """Computes the precision@k for the specified values of k"""
    maxk = max(topk)
    batch_size = target.size(0)

    _, pred = output.topk(maxk, 1, True, True)
    pred = pred.t()
    correct = pred.eq(target.reshape(1, -1).expand_as(pred)) # 이부분에서 view()로 하면 error가 남 ==> reshape으로 변경함

    res = []
    for k in topk:
        correct_k = correct[:k].reshape(-1).float().sum(0) # 이부분도 마찬가지
        res.append(correct_k.mul_(100.0 / batch_size))
    return res