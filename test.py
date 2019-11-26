import torch
import numpy
sample_prob = torch.FloatTensor(6).uniform_(0, 1)
sample_mask = sample_prob < 0.2
a = sample_mask.nonzero()
print(sample_mask)

b = numpy.array([[5,6,4],
                 [7,8,3]])
c = numpy.array([[5,6]])
e = c[-1,:]
d = b*c[-1,:, None]
print(d)
all_masks = numpy.array([[0,1,0]])
(finished,) = numpy.where(all_masks[-1] == 0) 
print(finished)

a = [1,4,3,7]
print(a[4-2:4])