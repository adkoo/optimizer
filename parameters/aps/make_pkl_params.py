# -*- coding: iso-8859-1 -*-

#How to make your own scan parameter file:
#1) On line 10, choose a unique filename.
#2) On lines 15-36, replace the expressions to the right of the assignment statements with the desired values (maintain formatting)
#3) Run this file from the /basic_gp_stuff/ directory.
#4)2019-10-30 clean up
import numpy as np
import epics
from epics import caget
import pickle

filename = 'tfgp_20191014_RBF.pkl'
#dict = {'LTS:H1:CurrentAO':25,'LTS:V1:CurrentAO':25,'LTS:H2:CurrentAO':25,'offst':0,'amp':1.0,'noise':0.01}
values=[0.33288468, 0.25384964, 0.44732893, 4.36670369, 0.284272 ,  0.38187369,  0.33507802 , 0.57132642,  0.22516421, 0.72504281, 0.92558641, 0.2516231,  0.2894494,  1.389410,  0.52856522, 0.29348572]
#values=[0.33288468, 0.25384964, 0.44732893, 1.15, 0.284272 ,  0.38187369,  0.33507802 , 0.57132642,  0.22516421, 0.72504281, 0.92558641, 0.2516231,  0.2894494,  1.389410,  0.52856522, 0.29348572]
sum=np.sum(values)
values_norm=values/sum
devices=['L1:RG2:QM1:CurrentAO', 'L1:RG2:QM2:CurrentAO', 'L1:RG2:QM3:CurrentAO',
       'L1:RG2:QM4:CurrentAO', 'L1:QM3:CurrentAO', 'L1:QM4:CurrentAO',
       'L1:RG2:SC1:VL:CurrentAO', 'L1:RG2:SC2:HZ:CurrentAO',
       'L1:RG2:SC2:VL:CurrentAO', 'L1:RG2:SC3:HZ:CurrentAO',
       'L1:RG2:SC3:VL:CurrentAO', 'L1:SC3:HZ:CurrentAO', 'L1:SC3:VL:CurrentAO',
       'L1:QM5:CurrentAO', 'L1:SC4:HZ:CurrentAO', 'L1:SC4:VL:CurrentAO']

dict={}
size=len(values)
for i in range(size):
    dict[devices[i]]=values[i]
dict['amp']=0.09861835988630561
dict['noise']=0.0004952875307346928

print('save to tfgp...')
print(dict)
f = open(filename,'wb')
pickle.dump(dict,f)
f.close()

values=[0.95840594,0.61396947,1.13269125,3.5741076,0.66072919,1.0447729,0.79725603,1.47640009,0.64536999,1.88449418,2.12452645,0.73626228,0.73887005,3.13302255,1.39235256,0.86731613]
dict={}
size=len(values)
for i in range(size):
    dict[devices[i]]=values[i]
dict['amp']=0.2056500034
dict['noise']=0.0004289255903

print('save to tfgp...')
print(dict)
f = open('tfgp_20191014_matern32.pkl','wb')
pickle.dump(dict,f)
f.close()

values=[0.54907808,0.3692215,0.68300124,5.72316315,0.40646845,0.59862485,0.49310135,0.86964679,0.37294076,1.07352829,1.31276087,0.42129018,0.42930714,1.97647295,0.81221186,0.5128272]
dict={}
size=len(values)
for i in range(size):
    dict[devices[i]]=values[i]
dict['amp']=0.1183856692
dict['noise']=0.0004459339408

print('save to tfgp...')
print(dict)
f = open('tfgp_20191014_matern52.pkl','wb')
pickle.dump(dict,f)
f.close()


#trained from new scanned data on 10-26-2019
values= [0.22078988,0.26574095,0.47829405,1.00406362,0.14711107,0.24826348,0.37638048,0.66085644,0.38513674,0.96105928,0.49242131,0.20863498,0.2242516,0.54836268,0.07952513,0.20008924]
#noise_param_variance 0.00019078093245028939
#amp 0.14740807434028955
dict['amp']=0.14740807434028955
dict['noise']=0.00019078093245028939
rows=len(values)
for i in range(rows):
    dict[devices[i]]=values[i]

f = open('tfgp_20191026_RBF.pkl','wb')
pickle.dump(dict,f)
f.close()



#matern52
#length_scale_param [0.5301943  0.57974298 0.93287674 1.55738394 0.2781559  0.48676285  0.62080341 1.00700028 0.63068022 1.33504816 0.85157653 0.38468695  0.34187084 0.90039229 0.12904501 0.39346024]
#noise_param_variance 0.00015752787526062437
#amp 0.16033151005207602
dict={}
values= [0.5301943,0.57974298,0.93287674,1.55738394,0.2781559,0.48676285,0.62080341,1.00700028,0.63068022,1.33504816,0.85157653,0.38468695,0.34187084,0.90039229,0.12904501,0.39346024]
dict['amp']=0.16033151005207602
dict['noise']=0.00015752787526062437
rows=len(values)
for i in range(rows):
    dict[devices[i]]=values[i]

f = open('tfgp_20191026_matern52.pkl','wb')
pickle.dump(dict,f)
f.close()



#matern32
#$length_scale_param [1.14104442 1.15166326 1.93485995 3.53009842 0.5435236  1.00184452  1.17587559 1.91437433 1.20989785 2.43048938 2.24330837 0.79114557  0.64170614 1.7408325  0.24202489 0.87199787]
#$noise_param_variance 0.00014944309862160857
#$amp 0.3057118422862669
dict={}
values=[1.14104442,1.15166326,1.93485995,3.53009842,0.5435236,1.00184452,1.17587559,1.91437433,1.20989785,2.43048938,2.24330837,0.79114557,0.64170614,1.7408325,0.24202489,0.87199787]
dict['amp']=0.3057118422862669
dict['noise']=0.00014944309862160857
rows=len(values)
for i in range(rows):
    dict[devices[i]]=values[i]

f = open('tfgp_20191026_matern32.pkl','wb')
pickle.dump(dict,f)
f.close()


#trained from new scanned data on 10-26-2019, remove steering magnets

devices1=['L1:RG2:QM1:CurrentAO', 'L1:RG2:QM2:CurrentAO', 'L1:RG2:QM3:CurrentAO',
       'L1:RG2:QM4:CurrentAO', 'L1:QM3:CurrentAO', 'L1:QM4:CurrentAO',
       'L1:RG2:SC1:VL:CurrentAO', 'L1:RG2:SC2:HZ:CurrentAO',
       'L1:RG2:SC2:VL:CurrentAO', 'L1:RG2:SC3:HZ:CurrentAO',
       'L1:RG2:SC3:VL:CurrentAO', 
       'L1:QM5:CurrentAO']

#got data from gp trainer
values = [0.8246469,  0.51113118, 0.52074331, 0.43801243, 0.31416264, 0.57697836,
 0.67361431, 0.51629454, 0.61509133, 0.42665865, 0.29098141, 0.34906042]
rows = len(values)
dict={}
for i in range(rows):
    dict[devices1[i]]=values[i]
dict['amp']=0.19788069543846426
dict['noise']=0.06565608478608254
#dict['noise']=0.00019  #change it manuall to see if it works
f = open('tfgp_20191026_RBF_nosteering.pkl','wb')
pickle.dump(dict,f)
f.close()

#above results are obtained with default gp kernel -- RBF

#matern32 kernel
#length_scale_param [0.28131369 0.31034553 0.60052556 0.64906617 0.21344806 0.33971465
# 0.36233996 0.35201099 0.32054675 0.54919454 0.57507362 0.44512081]
#noise_param_variance 0.05761468336008892
#amp 0.09213672488797832
values = [0.28131369,0.31034553,0.60052556,0.64906617,0.21344806,0.33971465,
 0.36233996,0.35201099,0.32054675,0.54919454,0.57507362,0.44512081]
dict={}
rows=len(values)
for i in range(rows):
    dict[devices1[i]]=values[i]
dict['amp']=0.09213672488797832
dict['noise']=0.05761468336008892
f = open('tfgp_20191026_matern32_nosteering.pkl','wb')
pickle.dump(dict,f)
f.close()


#matern52 kernel
#length_scale_param [0.21638666 0.27405066 0.49069129 0.49208349 0.20101479 0.28311935   0.30456699 0.28351084 0.27222831 0.49656042 0.43469106 0.37042972]
#noise_param_variance 0.05948358250077242
#amp 0.1077475822322336
values=[0.21638666,0.27405066,0.49069129,0.49208349,0.20101479,0.28311935,0.30456699,0.28351084,0.27222831,0.49656042,0.43469106,0.37042972]
#values=[0.73,0.27405066,0.49069129,0.49208349,0.20101479,0.28311935,0.30456699,0.28351084,0.27222831,0.49656042,0.43469106,0.37042972]
dict={}
rows=len(values)
for i in range(rows):
    dict[devices1[i]]=values[i]
dict['amp']=0.1077475822322336
dict['noise']=0.05948358250077242
f = open('tfgp_20191026_matern52_nosteering.pkl','wb')
pickle.dump(dict,f)
f.close()


#combine 10/14 optimization data and 10/26 scan data /home/oxygen/SHANG/ML_APS/linac/L3ChargeOpt/opt-scan-1014-1026.xls
#16 magnets
#RBF
values=[0.24971038,0.24490193,0.45699345,0.97297992,0.17487721,0.26567337,0.37209686,0.65248962,0.30703547,0.90474733,0.75147228,0.2227032,0.25184649,0.55466075,0.11101448,0.21843818]
dict={}
rows=len(values)
for i in range(rows):
    dict[devices[i]]=values[i]
dict['amp']=0.1262021733
dict['noise']=0.0002695605258
f = open('tfgp_20191014_1026_RBF.pkl','wb')
pickle.dump(dict,f)
f.close()

#matern52
values=[0.51214665,0.48110048,0.81999102,1.54183284,0.30177159,0.49942229,0.55309369,0.93705773,0.45985991,1.26207186,0.98024734,0.39016145,0.3532511,0.9193926,0.18280235,0.42117779]
dict={}
rows=len(values)
for i in range(rows):
    dict[devices[i]]=values[i]
dict['amp']=0.1439545448
dict['noise']=0.0002109903963
f = open('tfgp_20191014_1026_matern52.pkl','wb')
pickle.dump(dict,f)
f.close()

#matern32
values=[1.07022477,0.93354679,1.67322035,3.22587812,0.5736346,1.01722377,0.99742879,1.73075448,0.86538688,2.26070738,2.21487763,0.77684175,0.6217432,1.79983342,0.34600119,0.86584808]
dict={}
rows=len(values)
for i in range(rows):
    dict[devices[i]]=values[i]
dict['amp']=0.2954768632
dict['noise']=0.0001978023533
f = open('tfgp_20191014_1026_matern32.pkl','wb')
pickle.dump(dict,f)
f.close()

#12 magnets (no steering magnets)
#RBF
values=[0.63292721,0.34059407,0.53702173,0.61800174,0.31128117,0.55711319,0.29905284,0.52616939,0.47259304,0.46013766,0.4674393,0.44260775]
dict={}
rows=len(values)
for i in range(rows):
    dict[devices1[i]]=values[i]
dict['amp']=0.1251243992
dict['noise']=0.05296799903
f = open('tfgp_20191014_1026_RBF_nosteering.pkl','wb')
pickle.dump(dict,f)
f.close()

#matern52
values=[0.30823974,0.28222969,0.55869266,0.71698127,0.28021579,0.3611339,0.32149422,0.41768433,0.32538725,0.57953255,0.54075733,0.52191877]
dict={}
rows=len(values)
for i in range(rows):
    dict[devices1[i]]=values[i]
dict['amp']=0.08501787965
dict['noise']=0.04858748309
f = open('tfgp_20191014_1026_matern52_nosteering.pkl','wb')
pickle.dump(dict,f)
f.close()

#matern32
values=[0.3674013,0.31782013,0.66383077,0.88690924,0.30086013,0.42965852,0.37296711,0.47404646,0.38055838,0.68137019,0.65078568,0.60926786]
dict={}
rows=len(values)
for i in range(rows):
    dict[devices1[i]]=values[i]
dict['amp']=0.08022366695
dict['noise']=0.04663718527
f = open('tfgp_20191014_1026_matern32_nosteering.pkl','wb')
pickle.dump(dict,f)
f.close()

#add gaussian fit for 16 and 12
values=[0.7322836730022275, 0.4680323307269952, 1.0863090994868232, 2.464526634314797, 0.2275870574368614, 0.5218673479359833, 0.5311585257274893, 0.7224843830268624, 0.4620830977859818, 0.718981751508376, 4.039495633138642, 0.6769443976143563, 0.22242167458357542, 0.841175838942137, 1.8080668592247167, 0.24980528710636288]
dict={}
rows=len(values)
for i in range(rows):
    dict[devices[i]]=values[i]
dict['amp']=0.1474239004
dict['noise']=0.0001905386176
f = open('guassian_fit_sqrt2.pkl','wb')
pickle.dump(dict,f)
f.close()

values=[0.7322836730022275, 0.4680323307269952, 1.0863090994868232, 2.464526634314797, 0.2275870574368614, 0.5218673479359833, 0.5311585257274893, 0.7224843830268624, 0.4620830977859818, 0.718981751508376, 4.039495633138642, 0.841175838942137]
dict={}
rows=len(values)
for i in range(rows):
    dict[devices1[i]]=values[i]
dict['amp']=0.1978806954
dict['noise']=0.06565608479
f = open('guassian_fit_sqrt2_nosteering.pkl','wb')
pickle.dump(dict,f)
f.close()


#combine data from 10/14, 10/23, 10/26, 10/31 for 12 magnets (no steering)
#RBF
values=[0.58241933,0.29678635,0.48080855,3.43618106,0.26113353,0.52766097,0.40420108,0.30947095,0.26139892,0.52998378,0.5324202,0.50275636]
dict={}
rows=len(values)
for i in range(rows):
    dict[devices1[i]]=values[i]
dict['amp']=0.0473160192
dict['noise']=0.04756546522
f = open('tfgp_20191014-1023-1026-1031_RBF_nosteering.pkl','wb')
pickle.dump(dict,f)
f.close()

#matern32
values=[0.3707367,0.27209057,0.6268962,1.43793187,0.24651184,0.43000364,0.37451929,0.42389007,0.30644531,0.62692922,0.75646539,0.63878361]
dict={}
rows=len(values)
for i in range(rows):
    dict[devices1[i]]=values[i]
dict['amp']=0.04234193401
dict['noise']=0.0421605206
f = open('tfgp_20191014-1023-1026-1031_matern32_nosteering.pkl','wb')
pickle.dump(dict,f)
f.close()

#matern52
values=[0.34757096,0.2554463,0.56457023,1.31867706,0.23404222,0.39203008,0.34480126,0.3805012,0.28252844,0.56077706,0.6526772,0.57273871]
dict={}
rows=len(values)
for i in range(rows):
    dict[devices1[i]]=values[i]
dict['amp']=0.04389968406
dict['noise']=0.04318395429
f = open('tfgp_20191014-1023-1026-1031_matern52_nosteering.pkl','wb')
pickle.dump(dict,f)
f.close()

#combine scan data from 10/26 and 11/02  use 16 magnets training result
values=[0.24460295,0.22362762,0.45830581,1.02215592,0.17541322,0.2629256,0.40156738,0.64550455,0.38507488,0.94442535,0.59205422,0.11245807,0.13006519,0.5639242,0.09520972,0.14503264]
dict={}
size=len(values)
for i in range(size):
    dict[devices[i]]=values[i]
dict['amp']=0.1383661056
dict['noise']=0.0002073957334

f = open('tfgp_20191026_1102_RBF.pkl','wb')
pickle.dump(dict,f)
f.close()

values=[1.05632154,1.04639867,2.09340133,3.44036197,0.59046526,1.02350935,1.07453964,1.67478046,1.04249421,1.98035881,2.19496117,0.47265296,0.18988338,1.48930867,0.27471299,0.60230376]
dict={}
size=len(values)
for i in range(size):
    dict[devices[i]]=values[i]
dict['amp']=0.2030297871
dict['noise']=0.0001507962535

f = open('tfgp_20191026_1102_matern32.pkl','wb')
pickle.dump(dict,f)
f.close()

values=[0.53884009,0.51114462,0.9844945,1.58653231,0.31362723,0.53465091,0.60123543,0.94866029,0.60835154,1.18480441,0.95300433,0.2499934,0.12962675,0.83020415,0.14724226,0.27025624]

dict={}
size=len(values)
for i in range(size):
    dict[devices[i]]=values[i]
dict['amp']=0.124013177
dict['noise']=0.0001643861955

f = open('tfgp_20191026_1102_matern52.pkl','wb')
pickle.dump(dict,f)
f.close()


#opt-data optOnly.proc.xls
values=[0.46055728,0.25418915,0.81651849,5.09714797,0.27048728,0.48030383,0.70249861,0.60860195,0.33464074,9.2112687,11.35918962,0.28928856,0.29455499,0.80880964,0.29858179,0.22431606]
dict={}
size=len(values)
for i in range(size):
    dict[devices[i]]=values[i]
dict['amp']=0.07517625173
dict['noise']=0.004079985728

f = open('tfgp_optProc_RBF.pkl','wb')
pickle.dump(dict,f)
f.close()

values=[0.83853285,0.40720854,1.41944298,8.2454312,0.43448385,0.81999656,1.45599048,1.05916947,0.56073965,13.22223281,15.01524653,0.55398199,0.49313177,1.37838028,0.63297581,0.37976785]
dict={}
size=len(values)
for i in range(size):
    dict[devices[i]]=values[i]
dict['amp']=0.07940691064
dict['noise']=0.004014558862

f = open('tfgp_optProc_matern32.pkl','wb')
pickle.dump(dict,f)
f.close()

values=[0.61757356,0.31387079,1.04668222,6.18511423,0.3344641,0.61586292,1.01026489,0.79172582,0.42758114,9.70398238,11.42190251,0.39374697,0.369767,1.03753952,0.4223535,0.28690526]
dict={}
size=len(values)
for i in range(size):
    dict[devices[i]]=values[i]
dict['amp']=0.06754850461
dict['noise']=0.004040146915

f = open('tfgp_optProc_matern52.pkl','wb')
pickle.dump(dict,f)
f.close()

values=[0.48685483,0.20195869,0.76355163,4.38214481,0.33055641,0.22189541,0.17469478,0.34711856,0.08234131,0.96710108,10.91574036,0.99564102]
dict={}
size=len(values)
for i in range(size):
    dict[devices1[i]]=values[i]
dict['amp']=0.1026199388
dict['noise']=0.006419749544

f = open('tfgp_optProc_RBF_nosteering.pkl','wb')
pickle.dump(dict,f)
f.close()

values=[0.55574343,0.2742876,1.20436402,5.40402642,0.47466592,0.53501775,0.26611671,0.61417583,0.15149019,1.53371071,10.52644255,1.20268794]
dict={}
size=len(values)
for i in range(size):
    dict[devices1[i]]=values[i]
dict['amp']=0.07722922128
dict['noise']=0.006288352623

f = open('tfgp_optProc_matern32_nosteering.pkl','wb')
pickle.dump(dict,f)
f.close()

values=[0.49375694,0.22535605,0.96849818,4.63686355,0.41488649,0.3517582,0.21590121,0.4777094,0.11722306,1.22815629,9.98770212,1.06277979]
dict={}
size=len(values)
for i in range(size):
    dict[devices1[i]]=values[i]
dict['amp']=0.08039552445
dict['noise']=0.006327304725

f = open('tfgp_optProc_matern52_nosteering.pkl','wb')
pickle.dump(dict,f)
f.close()

#scan-data scanOnly.proc.xls
values=[0.35851194,0.38624931,0.78214125,1.32158094,0.18625156,0.30393168,0.39542564,0.7106069,0.44527183,0.99017824,1.2250136,0.08979221,0.10370003,0.80889183,0.16106338,0.35861723]
dict={}
size=len(values)
for i in range(size):
    dict[devices[i]]=values[i]
dict['amp']=0.1661711063
dict['noise']=0.003410675716

f = open('tfgp_scanProc_RBF.pkl','wb')
pickle.dump(dict,f)
f.close()

values=[0.92397127,0.9069247,1.65413333,2.44145901,0.3991683,0.74619509,0.93860215,1.50001105,0.74885859,2.03090242,1.40274817,0.25478028,0.19119658,1.35634232,0.39362026,0.69419913]
dict={}
size=len(values)
for i in range(size):
    dict[devices[i]]=values[i]
dict['amp']=0.172774059
dict['noise']=0.003167773593

f = open('tfgp_scanProc_matern32.pkl','wb')
pickle.dump(dict,f)
f.close()

values=[0.59948816,0.60784499,1.10210818,1.54694755,0.26040774,0.49166424,0.62718935,1.01084228,0.56503332,1.4013871,1.33922893,0.15361582,0.13738563,1.00648882,0.25248549,0.48196332]
dict={}
size=len(values)
for i in range(size):
    dict[devices[i]]=values[i]
dict['amp']=0.145770245
dict['noise']=0.003240525522

f = open('tfgp_scanProc_matern52.pkl','wb')
pickle.dump(dict,f)
f.close()

values=[0.36824843,0.29659679,0.68282134,1.5833632,0.19349611,0.13700332,0.27840729,0.6402455,0.37296952,0.13256622,16.585946,0.54931689]
dict={}
size=len(values)
for i in range(size):
    dict[devices1[i]]=values[i]
dict['amp']=0.06822094387
dict['noise']=0.02707179704

f = open('tfgp_scanProc_RBF_nosteeering.pkl','wb')
pickle.dump(dict,f)
f.close()


values=[0.83002894,0.59512665,1.43539712,3.12114595,0.33025082,0.26539368,0.38870194,1.14603439,0.64300734,0.22616973,36.59048677,1.01216158]
dict={}
size=len(values)
for i in range(size):
    dict[devices1[i]]=values[i]
dict['amp']=0.06827266133
dict['noise']=0.02674854173

f = open('tfgp_scanProc_mater32_nosteeering.pkl','wb')
pickle.dump(dict,f)
f.close()

values=[0.60490349,0.45274581,1.0759322,2.24443239,0.26232689,0.19902212,0.28814352,0.89325898,0.51153454,0.17928924,23.26730199,0.76597295]

dict={}
size=len(values)
for i in range(size):
    dict[devices1[i]]=values[i]
dict['amp']=0.06722437645
dict['noise']=0.02681506907

f = open('tfgp_scanProc_mater32_nosteeering.pkl','wb')
pickle.dump(dict,f)
f.close()


#training each scan and then combine, no scan data for SC4:VL, use it from the scan training result 10/26 scan data
#and use the scan data noise and amp for this one too.
values=[0.2771375179,0.3055148047,0.8720667561,1.416137807,0.1999111605,0.3879193105,0.2685487319,0.5984099864,0.309825375,0.4151262889,3.504133945,0.3648814736,0.1567526525,0.1555142438,0.6485822926,0.20008924]
dict['amp']=0.49
dict['noise']=0.003
rows=len(values)
for i in range(rows):
    dict[devices[i]]=values[i]

f = open('tfgp_20191026com_RBF.pkl','wb')
pickle.dump(dict,f)
f.close()

