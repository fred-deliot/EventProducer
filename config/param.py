#dicts
lhe_dic='/afs/cern.ch/work/h/helsens/public/FCCDicts/LHEdict.json'
fcc_dic='/afs/cern.ch/work/h/helsens/public/FCCDicts/PythiaDelphesdict_v0_0.json'
readlhe_dic='/afs/cern.ch/work/h/helsens/public/FCCDicts/readLHE.json'
readfcc_dic='/afs/cern.ch/work/h/helsens/public/FCCDicts/readFCC.json'

gp_dir  = '/eos/fcc/hh/generation/mg5_amcatnlo/gridpacks/'
lhe_dir = '/eos/fcc/hh/generation/mg5_amcatnlo/lhe/'
delphes_dir = '/eos/fcc/hh/generation/DelphesEvents/'

delphescards_dir = '/eos/fcc/hh/delphescards/'

fccsw_dir='/cvmfs/fcc.cern.ch/sw/0.8/'
stack=fccsw_dir+'init_fcc_stack.sh'
fccsw=fccsw_dir+'fccsw/0.8/x86_64-slc6-gcc49-dbg/'

gridpacklist = {
'pp_w012j_5f':['w + 0,1,2 jets 5 flavor scheme','inclusive','xqcut = 30, qCut = 45','1.4995e06','0.724'],
'pp_z012j_5f':['z + 0,1,2 jets 5 flavor scheme','inclusive','xqcut = 30, qCut = 45','5.1839e05','0.691'],
'pp_jjaa01j_5f':['dijet diphoton + 0,1 jets 5 flavor scheme','','xqcut = 20, qCut = 30','55.72','0.236'],
'pp_jjaa_5f':['dijet diphoton','','','17.97','1.0'],
'pp_jjja01j_5f':['photon +jets + 0,1 jets 5 flavor scheme','','xqcut = 20, qCut = 25','4.133e+05','0.143'],
'pp_jjja_5f':['photon +jets','','','1.023e05','1.0'],
'pp_jjaa_4f':['dijet diphoton 4 flavor scheme','','','431.2','1.0'],
'pp_bbja_4f':['bbja 4 flavor scheme','','','4679','1.0'],
'pp_bbaa01j_4f':['bbaa + 0,1 jets 4 flavor scheme','','xqcut = 25, qCut = 35','5.899','0.312'],
'pp_bjaa01j_4f':['bjaa + 0,1 jets 4 flavor scheme','','xqcut = 25, qCut = 35','16.9','0.335'],
'pp_z012j_5f':['z + 0,1,2 jets 5 flavor scheme','inclusive','xqcut = 30, qCut = 45','5.1839e05','0.691'],
'pp_tth':['ttbar plus higgs','inclusive','','23.37','1.0'],
'pp_bbh':['bbar plus higgs','inclusive','50 < mbb < 300','0.916','1.0'],
'pp_zh':['z plus higgs production','inclusive','','7.42','1.0'],
'pp_hh':['gluon gluon fusion di-higgs','inclusive','','0.65','1.0'],
'pp_vbf_hh':['vector boson fusion di-higgs','inclusive','','0.06612','1.0'],
'pp_vbf_v01j_5f_HT_0_2000':['vbf vector boson + 0/1 jets','0 < HT < 2000','xqcut = 40, qCut = 60','1.151e+07','1.0'],
'pp_vbf_v01j_5f_HT_2000_4000':['vbf vector boson + 0/1 jets','2000 < HT < 4000','xqcut = 40, qCut = 60','1.912e+04','1.0'],
'pp_vbf_v01j_5f_HT_4000_7200':['vbf vector boson + 0/1 jets','4000 < HT < 7200','xqcut = 40, qCut = 60','400.9','1.0'],
'pp_vbf_v01j_5f_HT_7200_100000':['vbf vector boson + 0/1 jets','7200 < HT < 100000','xqcut = 40, qCut = 60','72.31','1.0'],
'pp_t123j_5f_HT_0_1900':['single top (s,t channels)+ 0/1/2/3 jets','0 < HT < 1900','xqcut = 40, qCut = 60','7490','1.0'],
'pp_t123j_5f_HT_1900_3500':['single top (s,t channels)+ 0/1/2/3 jets','1900 < HT < 3500','xqcut = 40, qCut = 60','13.65','1.0'],
'pp_t123j_5f_HT_3500_5900':['single top (s,t channels)+ 0/1/2/3 jets','3500 < HT < 5900','xqcut = 40, qCut = 60','1.371','1.0'],
'pp_t123j_5f_HT_5900_100000':['single top (s,t channels)+ 0/1/2/3 jets','5900 < HT < 100000','xqcut = 40, qCut = 60','0.175','1.0'],
'pp_t123j_5f':['single top (s,t channels)+ 1/2/3 jets','inclusive','xqcut = 40, qCut = 60','7524','1.0'],
'pp_vh012j_5f_HT_0_300':['higgsstrahlung + 0/1/2 jets','0 < HT < 300','xqcut = 40, qCut = 60','25.24','1.0'],
'pp_vh012j_5f_HT_300_1400':['higgsstrahlung + 0/1/2 jets','300 < HT < 1400','xqcut = 40, qCut = 60','11.7','1.0'],
'pp_vh012j_5f_HT_1400_2900':['higgsstrahlung + 0/1/2 jets','1400 < HT < 2900','xqcut = 40, qCut = 60','0.3437','1.0'],
'pp_vh012j_5f_HT_2900_5300':['higgsstrahlung + 0/1/2 jets','2900 < HT < 5300','xqcut = 40, qCut = 60','0.03349','1.0'],
'pp_vh012j_5f_HT_5300_8800':['higgsstrahlung + 0/1/2 jets','5300 < HT < 8800','xqcut = 40, qCut = 60','0.003608','1.0'],
'pp_vh012j_5f_HT_8800_100000':['higgsstrahlung + 0/1/2 jets','8800 < HT < 100000','xqcut = 40, qCut = 60','0.0004647','1.0'],
'pp_vh012j_5f':['higgsstrahlung + 0/1/2 jets','inclusive','xqcut = 40, qCut = 60','37.43','0.544'],
'pp_llv01j_5f_HT_0_800':[' di-vector with V -> ll (l=e,mu,ve,vm,vt) + 0/1 jets','0 < HT < 800','xqcut = 40, qCut = 60','108.7','1.0'],
'pp_llv01j_5f_HT_800_2000':[' di-vector with V -> ll (l=e,mu,ve,vm,vt) + 0/1 jets','800 < HT < 2000','xqcut = 40, qCut = 60','0.9956','1.0'],
'pp_llv01j_5f_HT_2000_4000':[' di-vector with V -> ll (l=e,mu,ve,vm,vt) + 0/1 jets','2000 < HT < 4000','xqcut = 40, qCut = 60','0.07411','1.0'],
'pp_llv01j_5f_HT_4000_100000':[' di-vector with V -> ll (l=e,mu,ve,vm,vt) + 0/1 jets','4000 < HT < 100000','xqcut = 40, qCut = 60','0.008311','1.0'],
'pp_llv01j_5f':[' di-vector with V -> ll (l=e,mu,ve,vm,vt) + 0/1 jets','inclusive','xqcut = 40, qCut = 60','110.3','0.779'],
'pp_tt012j_5f_HT_0_600':['top pair + 0/1/2 jets','0 < HT < 600','xqcut = 60, qCut = 90','3.207e+04','1.0'],
'pp_tt012j_5f_HT_600_1200':['top pair + 0/1/2 jets','600 < HT < 1200','xqcut = 60, qCut = 90','8915','1.0'],
'pp_tt012j_5f_HT_1200_2100':['top pair + 0/1/2 jets','1200 < HT < 2100','xqcut = 60, qCut = 90','1743','1.0'],
'pp_tt012j_5f_HT_2100_3400':['top pair + 0/1/2 jets','2100 < HT < 3400','xqcut = 60, qCut = 90','284.4','1.0'],
'pp_tt012j_5f_HT_3400_5300':['top pair + 0/1/2 jets','3400 < HT < 5300','xqcut = 60, qCut = 90','44.76','1.0'],
'pp_tt012j_5f_HT_5300_8100':['top pair + 0/1/2 jets','5300 < HT < 8100','xqcut = 60, qCut = 90','6.428','1.0'],
'pp_tt012j_5f_HT_8100_100000':['top pair + 0/1/2 jets','8100 < HT < 100000','xqcut = 60, qCut = 90','0.8705','1.0'],
'pp_tt012j_5f':['top pair + 0/1/2 jets','inclusive','xqcut = 60, qCut = 90','4.2670e04','0.468'],
'pp_vbf_h01j_5f_HT_0_2000':['vbf higgs + 0/1 jets','0 < HT < 2000','xqcut = 40, qCut = 60','83.91','1.0'],
'pp_vbf_h01j_5f_HT_2000_4000':['vbf higgs + 0/1 jets','2000 < HT < 4000','xqcut = 40, qCut = 60','0.07215','1.0'],
'pp_vbf_h01j_5f_HT_4000_7200':['vbf higgs + 0/1 jets','4000 < HT < 7200','xqcut = 40, qCut = 60','0.003946','1.0'],
'pp_vbf_h01j_5f_HT_7200_100000':['vbf higgs + 0/1 jets','7200 < HT < 100000','xqcut = 40, qCut = 60','0.000268','1.0'],
'pp_vbf_h01j_5f':['vbf vector boson + 0/1 jets','inclusive','xqcut = 40, qCut = 60','84.17','0.187'],
'pp_v0123j_5f_HT_0_1500':['vector boson + 0/1/2/3 jets','0 < HT < 1500','xqcut = 30, qCut = 45','8.889e+06','1.0'],
'pp_v0123j_5f_HT_1500_2900':['vector boson + 0/1/2/3 jets','1500 < HT < 2900','xqcut = 30, qCut = 45','2868','1.0'],
'pp_v0123j_5f_HT_2900_5100':['vector boson + 0/1/2/3 jets','2900 < HT < 5100','xqcut = 30, qCut = 45','300.8','1.0'],
'pp_v0123j_5f_HT_5100_8500':['vector boson + 0/1/2/3 jets','5100 < HT < 8500','xqcut = 30, qCut = 45','30.93','1.0'],
'pp_v0123j_5f_HT_8500_100000':['vector boson + 0/1/2/3 jets','8500 < HT < 100000','xqcut = 30, qCut = 45','2.95','1.0'],
'pp_v0123j_5f':['vector boson + 0/1/2/3 jets','inclusive','xqcut = 30, qCut = 45','8.886e+06','0.232'],
'pp_vbf_hh01j_5f_HT_0_2000':['vbf di-higgs + 0/1 jets','0 < HT < 2000','xqcut = 60, qCut = 90','0.01087','1.0'],
'pp_vbf_hh01j_5f_HT_2000_4000':['vbf di-higgs + 0/1 jets','2000 < HT < 4000','xqcut = 60, qCut = 90','0.0003602','1.0'],
'pp_vbf_hh01j_5f_HT_4000_7200':['vbf di-higgs + 0/1 jets','4000 < HT < 7200','xqcut = 60, qCut = 90','4.4e-05','1.0'],
'pp_vbf_hh01j_5f_HT_7200_100000':['vbf di-higgs + 0/1 jets','7200 < HT < 100000','xqcut = 60, qCut = 90','5.737e-06','1.0'],
'pp_vbf_hh01j_5f':['vbf di-higgs + 0/1 jets','inclusive','xqcut = 60, qCut = 90','0.005843','1.0'],
'pp_vv012j_5f_HT_0_300':['di-vector boson + 0/1/2 jets','0 < HT < 300','xqcut = 40, qCut = 60','3.147e+04','1.0'],
'pp_vv012j_5f_HT_300_1400':['di-vector boson + 0/1/2 jets','300 < HT < 1400','xqcut = 40, qCut = 60','2233','1.0'],
'pp_vv012j_5f_HT_1400_2900':['di-vector boson + 0/1/2 jets','1400 < HT < 2900','xqcut = 40, qCut = 60','71.51','1.0'],
'pp_vv012j_5f_HT_2900_5300':['di-vector boson + 0/1/2 jets','2900 < HT < 5300','xqcut = 40, qCut = 60','7.973','1.0'],
'pp_vv012j_5f_HT_5300_8800':['di-vector boson + 0/1/2 jets','5300 < HT < 8800','xqcut = 40, qCut = 60','0.9271','1.0'],
'pp_vv012j_5f_HT_8800_100000':['di-vector boson + 0/1/2 jets','8800 < HT < 100000','xqcut = 40, qCut = 60','0.1247','1.0'],
'pp_vv012j_5f':['di-vector boson + 0/1/2 jets','inclusive','xqcut = 40, qCut = 60','3.39e+04','0.458'],
'pp_tv012j_5f_HT_0_500':['top pair off-shell t* -> Wj + 0/1/2 jets','0 < HT < 500','xqcut = 60, qCut = 90','3000','1.0'],
'pp_tv012j_5f_HT_500_1500':['top pair off-shell t* -> Wj + 0/1/2 jets','500 < HT < 1500','xqcut = 60, qCut = 90','1124','1.0'],
'pp_tv012j_5f_HT_1500_2800':['top pair off-shell t* -> Wj + 0/1/2 jets','1500 < HT < 2800','xqcut = 60, qCut = 90','72.13','1.0'],
'pp_tv012j_5f_HT_2800_4700':['top pair off-shell t* -> Wj + 0/1/2 jets','2800 < HT < 4700','xqcut = 60, qCut = 90','7.738','1.0'],
'pp_tv012j_5f_HT_4700_7400':['top pair off-shell t* -> Wj + 0/1/2 jets','4700 < HT < 7400','xqcut = 60, qCut = 90','0.7973','1.0'],
'pp_tv012j_5f_HT_7400_100000':['top pair off-shell t* -> Wj + 0/1/2 jets','7400 < HT < 100000','xqcut = 60, qCut = 90','0.09901','1.0'],
'pp_tv012j_5f':['top pair off-shell t* -> Wj + 0/1/2 jets','inclusive','xqcut = 60, qCut = 90','4210','0.461'],
'pp_tth01j_5f_HT_0_1100':['higgs associated with top pair + 0/1 jets','0 < HT < 1100','xqcut = 80, qCut = 120','36.94','1.0'],
'pp_tth01j_5f_HT_1100_2700':['higgs associated with top pair + 0/1 jets','1100 < HT < 2700','xqcut = 80, qCut = 120','7.466','1.0'],
'pp_tth01j_5f_HT_2700_4900':['higgs associated with top pair + 0/1 jets','2700 < HT < 4900','xqcut = 80, qCut = 120','0.4224','1.0'],
'pp_tth01j_5f_HT_4900_8100':['higgs associated with top pair + 0/1 jets','4900 < HT < 8100','xqcut = 80, qCut = 120','0.0336','1.0'],
'pp_tth01j_5f_HT_8100_100000':['higgs associated with top pair + 0/1 jets','8100 < HT < 100000','xqcut = 80, qCut = 120','0.002924','1.0'],
'pp_tth01j_5f':['higgs associated with top pair + 0/1 jets','inclusive','xqcut = 80, qCut = 120','44.84','0.612'],
'pp_hh01j_5f_HT_0_300':['gluon fusion di-higgs + 0/1 jets','0 < HT < 300','xqcut = 60, qCut = 90','0.3501','1.0'],
'pp_hh01j_5f_HT_300_1400':['gluon fusion di-higgs + 0/1 jets','300 < HT < 1400','xqcut = 60, qCut = 90','0.7453','1.0'],
'pp_hh01j_5f_HT_1400_2900':['gluon fusion di-higgs + 0/1 jets','1400 < HT < 2900','xqcut = 60, qCut = 90','0.01262','1.0'],
'pp_hh01j_5f_HT_2900_5300':['gluon fusion di-higgs + 0/1 jets','2900 < HT < 5300','xqcut = 60, qCut = 90','0.0007101','1.0'],
'pp_hh01j_5f_HT_8800_100000':['gluon fusion di-higgs + 0/1 jets','8800 < HT < 100000','xqcut = 60, qCut = 90','2.703e-06','1.0'],
'pp_ttv01j_5f_HT_0_1100':['top pair + boson + 0/1 jets','0 < HT < 1100','xqcut = 80, qCut = 120','222','1.0'],
'pp_ttv01j_5f_HT_1100_2700':['top pair + boson + 0/1 jets','1100 < HT < 2700','xqcut = 80, qCut = 120','32.88','1.0'],
'pp_ttv01j_5f_HT_2700_4900':['top pair + boson + 0/1 jets','2700 < HT < 4900','xqcut = 80, qCut = 120','2.163','1.0'],
'pp_ttv01j_5f_HT_4900_8100':['top pair + boson + 0/1 jets','4900 < HT < 8100','xqcut = 80, qCut = 120','0.2143','1.0'],
'pp_ttv01j_5f_HT_8100_100000':['top pair + boson + 0/1 jets','8100 < HT < 100000','xqcut = 80, qCut = 120','0.02413','1.0'],
'pp_ll012j_5f_HT_0_200':['V -> ll (l=e,mu,ve,vm,vt) + ','0 < HT < 200','xqcut = 30, qCut = 45','1.158e+04','1.0'],
'pp_ll012j_5f_HT_200_700':['V -> ll (l=e,mu,ve,vm,vt) + ','200 < HT < 700','xqcut = 30, qCut = 45','694.2','1.0'],
'pp_ll012j_5f_HT_700_1500':['V -> ll (l=e,mu,ve,vm,vt) + ','700 < HT < 1500','xqcut = 30, qCut = 45','15.55','1.0'],
'pp_ll012j_5f_HT_1500_2700':['V -> ll (l=e,mu,ve,vm,vt) + ','1500 < HT < 2700','xqcut = 30, qCut = 45','1.03','1.0'],
'pp_ll012j_5f_HT_2700_4200':['V -> ll (l=e,mu,ve,vm,vt) + ','2700 < HT < 4200','xqcut = 30, qCut = 45','0.1166','1.0'],
'pp_ll012j_5f_HT_4200_100000':['V -> ll (l=e,mu,ve,vm,vt) + ','4200 < HT < 100000','xqcut = 30, qCut = 45','0.02784','1.0'],
'pp_ll012j_5f':['V -> ll (l=e,mu,ve,vm,vt) + ','inclusive','xqcut = 30, qCut = 45','1.235e+04','0.83'],
'pp_h012j_5f_HT_0_100':['gluon fusion higgs (finite mt) + 0/1/2 jets','0 < HT < 100','xqcut = 30, qCut = 45','313.4','0.404'],
'pp_h012j_5f_HT_100_400':['gluon fusion higgs (finite mt) + 0/1/2 jets','100 < HT < 400','xqcut = 30, qCut = 45','220.7','1.0'],
'pp_h012j_5f_HT_400_1000':['gluon fusion higgs (finite mt) + 0/1/2 jets','400 < HT < 1000','xqcut = 30, qCut = 45','47.27','1.0'],
'pp_h012j_5f_HT_1000_1900':['gluon fusion higgs (finite mt) + 0/1/2 jets','1000 < HT < 1900','xqcut = 30, qCut = 45','3.587','1.0'],
'pp_h012j_5f_HT_1900_4400':['gluon fusion higgs (finite mt) + 0/1/2 jets','1900 < HT < 4400','xqcut = 30, qCut = 45','0.2767','1.0'],
'pp_h012j_5f_HT_4400_8500':['gluon fusion higgs (finite mt) + 0/1/2 jets','4400 < HT < 8500','xqcut = 30, qCut = 45','0.003932','1.0'],
'pp_h012j_5f_HT_8500_100000':['gluon fusion higgs (finite mt) + 0/1/2 jets','8500 < HT < 100000 < ','xqcut = 30, qCut = 45','6.368e-05','1.0'],
'pp_h012j_5f':['gluon fusion higgs (finite mt) + 0/1/2 jets','inclusive','xqcut = 30, qCut = 45','587.5','0.363'],
'pp_vvv01j_5f_HT_0_1200':['tri-vector boson + 0/1 jets','0 < HT < 1200','xqcut = 60, qCut = 90','73.04','1.0'],
'pp_vvv01j_5f_HT_1200_3000':['tri-vector boson + 0/1 jets','1200 < HT < 3000','xqcut = 60, qCut = 90','2.093','1.0'],
'pp_vvv01j_5f_HT_3000_6000':['tri-vector boson + 0/1 jets','3000 < HT < 6000','xqcut = 60, qCut = 90','0.2028','1.0'],
'pp_vvv01j_5f_HT_6000_100000':['tri-vector boson + 0/1 jets','6000 < HT < 100000','xqcut = 60, qCut = 90','0.02111','1.0'],
'pp_vvv01j_5f':['tri-vector boson + 0/1 jets','inclusive','xqcut = 60, qCut = 90','75.87','0.525'],
'gg_aa01j_5f_HT_0_500':['gluon fusion di-photon + 0/1 jets','0 < HT < 500','xqcut = 20, qCut = 30','850.4','1.0'],
'gg_aa01j_5f_HT_500_1000':['gluon fusion di-photon + 0/1 jets','500 < HT < 1000','xqcut = 20, qCut = 30','0.5129','1.0'],
'gg_aa01j_5f_HT_1000_2000':['gluon fusion di-photon + 0/1 jets','1000 < HT < 2000','xqcut = 20, qCut = 30','0.04734','1.0'],
'gg_aa01j_5f_HT_2000_4000':['gluon fusion di-photon + 0/1 jets','2000 < HT < 4000','xqcut = 20, qCut = 30','0.00291','1.0'],
'gg_aa01j_5f_HT_4000_7200':['gluon fusion di-photon + 0/1 jets','4000 < HT < 7200','xqcut = 20, qCut = 30','8.602e-05','1.0'],
'gg_aa01j_5f_HT_7200_100000':['gluon fusion di-photon + 0/1 jets','7200 < HT < 100000','xqcut = 20, qCut = 30','4.357e-06','1.0'],
'gg_aa01j_5f':['gluon fusion di-photon + 0/1 jets','inclusive','xqcut = 20, qCut = 30','848.2','0.576'],
'gg_aa01j_5f_HT_500_1000':['gluon fusion di-photon + 0/1 jets','500 < HT < 1000','xqcut = 20, qCut = 30','848.2','0.576'],
'pp_aa012j_5f':['di-photon + 0/1/2 jets','inclusive','xqcut = 20, qCut = 30','7030','0.307'],
'pp_aj012j_5f':['photon + jet + 0/1/2 jets','inclusive','xqcut = 20, qCut = 30','6.759e+06','0.133'],
'pp_jj012j_5f':['di-jet + 0/1/2 jets','inclusive','xqcut = 20, qCut = 30','6.563e+09','0.141'],
'pp_hh01j_5f':['gluon fusion di-higgs + 0/1 jets','inclusive','xqcut = 60, qCut = 90','1.113','1.0'],
'pp_llll_5f':['Z/gamma* Z/gamma* to 4l','inclusive','xqcut = 40, qCut = 60','0.6045','1.0'],
'pp_llll01j_5f':['Z/gamma* Z/gamma* to 4l','inclusive','xqcut = 40, qCut = 60','0.899','1.0'],
}
