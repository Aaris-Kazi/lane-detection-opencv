import numpy as np
import pandas as pd
import time
def combo(lane_image, lines):
    # print(lane_image)
    print(lines)
    x1= []
    x2= []
    y1= []
    y2= []
    for line in lines:
        a1, a2, b1, b2 = line.reshape(4)
        x1.append(a1)
        x2.append(a2)
        y1.append(b1)
        y2.append(b2)
    # df = pd.DataFrame({
    #     "X1": x1,
    #     "X2": x2,
    #     "Y1": y1,
    #     "Y2": y2,
    # })
    i = time.time()
    filename = "image %.2f" % i
    print(filename)
    
    # df.to_csv(filename)