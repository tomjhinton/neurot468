from pony.orm import db_session
from app import db
from models.Work import Work, WorkSchema
import base64

from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import random
img = Image.new('RGBA', (6000, 6000), color='white')
thing = 1
import os
import io
import sys
import numpy as np
from PIL import Image
import matplotlib.pylab as plt
import matplotlib.colors as mclr
from random import randint
def random_color():
    rgbl=[255,0,0]
    random.shuffle(rgbl)
    return tuple(rgbl)


def draw_pastell(nx=900, ny=1600, CL=180, rshift=3):
    nz=3
    mid = nx//2
    dCL = 50
    #---- start the coloring ----------
    A = np.ones((nx,ny,nz)) *CL           # initialize the image matrix
    #np.random.seed(1234)                  # initialize RNG

    #---- initialize the lower part ----
    ix = slice(0,mid-1);   iz = slice(0,nz)  # color the left boundary
    A[ix,0,iz] =  CL + np.cumsum(np.random.randint(-rshift, rshift+1, size=(mid-1,nz)),axis=0 )

    #---- initialize the upper part ----
    ix = slice(mid,nx);   iz = slice(0,nz)  # color the left boundary
    A[ix,0,iz] =  CL-dCL + np.cumsum(np.random.randint(-rshift, rshift+1, size=(nx-mid,nz)),axis=0 )

    #---- march to the right boundary -------------
    ix = slice(1,nx-1); ixm = slice(0,nx-2); ixp = slice(2,nx)
    for jy in range(1,ny):                # smear the color to the right boundary
        A[ix,jy,iz] = 0.3333*(A[ixm,jy-1,iz] + A[ix,jy-1,iz] + A[ixp,jy-1,iz]) + np.random.randint(-rshift, rshift+1, size=(nx-2,nz))

    #---- show&save grafics ---------
    im1 = Image.fromarray(A.astype(np.uint8)).convert('RGBA')
    

    buf = io.BytesIO()
    im1.save(buf, format='PNG')
    thing = buf.getvalue()
    db.drop_all_tables(with_all_data=True)
    db.create_tables()
    with db_session():







        Work(
        dat=str(base64.b64encode(buf.getvalue()))

        ),











        db.commit()


draw_pastell(nx=900, ny=1600, CL=181, rshift=3)
