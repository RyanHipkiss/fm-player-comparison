import json

class Player:
    def __init__(self, row):
        self.name = row[0]
        self.position = row[1]
        self.age = int(row[2])
        self.nationality = row[3]
        self.height = row[4]
        self.weight = row[5]
        self.personality = row[6]
        self.club = row[7]
        self.transfer_value = row[8]
        self.av_rat = self._castToFloat(row[9])
        self.gls = self._castToFloat(row[10]) 
        self.xg = self._castToFloat(row[11]) 
        self.pens_s = self._castToFloat(row[12]) 
        self.pen_r = self._castToFloat(row[13]) 
        self.shot_90 = self._castToFloat(row[14]) 
        self.shot_pct = self._castToFloat(row[15]) 
        self.sht_90 = self._castToFloat(row[16]) 
        self.asts_90 = self._castToFloat(row[17]) 
        self.ps_c_90 = self._castToFloat(row[18]) 
        self.pas_pct = self._castToFloat(row[19]) 
        self.k_ps_90 = self._castToFloat(row[20]) 
        self.ccc = self._castToFloat(row[21]) 
        self.cr_a = self._castToFloat(row[22]) 
        self.cr_c_a = self._castToFloat(row[23]) 
        self.tck_90 = self._castToFloat(row[24]) 
        self.tck_r = self._castToFloat(row[25]) 
        self.k_tck = self._castToFloat(row[26]) 
        self.int_90 = self._castToFloat(row[27]) 
        self.clear = self._castToFloat(row[28]) 
        self.fls = self._castToFloat(row[29]) 
        self.aer_a_90 = self._castToFloat(row[30]) 
        self.hdrs_w_90 = self._castToFloat(row[31]) 
        self.hdr_pct = self._castToFloat(row[32]) 
        self.gl_mst = self._castToFloat(row[33]) 
        self.drb_90 = self._castToFloat(row[34]) 
        self.fa = self._castToFloat(row[35]) 
        self.dist_90 = self._castToFloat(row[36]) 
        self.yel = self._castToFloat(row[37]) 
        self.red = self._castToFloat(row[38]) 
        self.off = self._castToFloat(row[39]) 
        self.apps = self._castToFloat(row[40]) 
        self.mins = self._castToFloat(row[41]) 
        self.shots = self._castToFloat(row[42]) 
        self.ast = self._castToFloat(row[43]) 
        self.pens = self._castToFloat(row[44]) 
        self.mins_gm = self._castToFloat(row[45]) 
        self.sht = self._castToFloat(row[46]) 
        self.hdrs_a = self._castToFloat(row[47]) 
        self.cr_c = self._castToFloat(row[48]) 
        self.distance = self._castToFloat(row[49]) 
        self.drb = self._castToFloat(row[50]) 
        self.hdrs = self._castToFloat(row[51]) 
        self.itc = self._castToFloat(row[52]) 
        self.k_pas = self._castToFloat(row[53]) 
        self.pas_a = self._castToFloat(row[54]) 
        self.ps_c = self._castToFloat(row[55]) 
        self.tck_a = self._castToFloat(row[56]) 
        self.tck_c = self._castToFloat(row[57]) 
        self.expires = self._castToFloat(row[58]) 
        self.salary = self._castToFloat(row[59]) 
        self.preferred_foot = self._castToFloat(row[60]) 
        self.acc = self._attributeMasking(row[61]) 
        self.aer = self._attributeMasking(row[62]) 
        self.agg = self._attributeMasking(row[63]) 
        self.agi = self._attributeMasking(row[64]) 
        self.ant = self._attributeMasking(row[65]) 
        self.bal = self._attributeMasking(row[66]) 
        self.bra = self._attributeMasking(row[67]) 
        self.cmd = self._attributeMasking(row[68]) 
        self.com = self._attributeMasking(row[69]) 
        self.cmp = self._attributeMasking(row[70]) 
        self.cnt = self._attributeMasking(row[71]) 
        self.cor = self._attributeMasking(row[72]) 
        self.cro = self._attributeMasking(row[73]) 
        self.dec = self._attributeMasking(row[74]) 
        self.det = self._attributeMasking(row[75]) 
        self.dri = self._attributeMasking(row[76]) 
        self.ecc = self._attributeMasking(row[77]) 
        self.fin = self._attributeMasking(row[78]) 
        self.fir = self._attributeMasking(row[79]) 
        self.fla = self._attributeMasking(row[80]) 
        self.fre = self._attributeMasking(row[81]) 
        self.han = self._attributeMasking(row[82]) 
        self.hea = self._attributeMasking(row[83]) 
        self.jum = self._attributeMasking(row[84]) 
        self.kic = self._attributeMasking(row[85]) 
        self.ldr = self._attributeMasking(row[86]) 
        self.lon = self._attributeMasking(row[87]) 
        self.l_th = self._attributeMasking(row[88]) 
        self.mar = self._attributeMasking(row[89]) 
        self.nat = self._attributeMasking(row[90]) 
        self.otb = self._attributeMasking(row[91]) 
        self.one_v_one = self._attributeMasking(row[92]) 
        self.pac = self._attributeMasking(row[93]) 
        self.pas = self._attributeMasking(row[94]) 
        self.pen = self._attributeMasking(row[95]) 
        self.pos = self._attributeMasking(row[96]) 
        self.pun = self._attributeMasking(row[97]) 
        self.ref = self._attributeMasking(row[98]) 
        self.tro = self._attributeMasking(row[99]) 
        self.sta = self._attributeMasking(row[100]) 
        self.str = self._attributeMasking(row[101]) 
        self.tck = self._attributeMasking(row[102]) 
        self.tea = self._attributeMasking(row[103]) 
        self.tec = self._attributeMasking(row[104]) 
        self.thr = self._attributeMasking(row[105]) 
        self.vis = self._attributeMasking(row[106]) 
        self.wor = self._attributeMasking(row[107]) 
        self.k_hdrs_90 = self._castToFloat(row[108]) 
        self.blk_90 = self._castToFloat(row[109]) 
        self.xg_shot = self._castToFloat(row[110]) 
        self.sprints_90 = self._castToFloat(row[111]) 
        self.poss_won_90 = self._castToFloat(row[112]) 
        self.poss_lost_90 = self._castToFloat(row[113]) 
        self.pres_a_90 = self._castToFloat(row[114]) 
        self.pres_c_90 = self._castToFloat(row[115]) 
        self.pr_passes_90 = self._castToFloat(row[116]) 
        self.xa_90 = self._castToFloat(row[117]) 
        self.blk = self._castToFloat(row[118]) 
        self.xgp = self._castToFloat(row[119]) 
        self.xsv_pct = self._castToFloat(row[120]) 
        self.conv_pct = self._castToFloat(row[121]) 
        self.op_kp_90 = self._castToFloat(row[122]) 
        self.svt = self._castToFloat(row[123]) 
        self.xgp_90 = self._castToFloat(row[124]) 
        self.op_kp = self._castToFloat(row[125]) 
        self.sv_pct = self._castToFloat(row[126]) 
        self.svh = self._castToFloat(row[127]) 
        self.svp = self._castToFloat(row[128]) 
        self.all_90 = self._castToFloat(row[129]) 
        self.cln_90 = self._castToFloat(row[130]) 
        self.np_xg_90 = self._castToFloat(row[131]) 
        self.pens_saved_ratio = self._castToFloat(row[132]) 
        self.np_xg = self._castToFloat(row[133]) 
        self.division = self._castToFloat(row[134]) 
        self.style = self._castToFloat(row[135]) 
        self.media_description = self._castToFloat(row[136]) 
        self.media_handling = self._castToFloat(row[137]) 
        self.fk_shots = self._castToFloat(row[138]) 
        self.ch_c_90 = self._castToFloat(row[139]) 
        self.clr_90 = self._castToFloat(row[140]) 
        self.crs_a_90 = self._castToFloat(row[141]) 
        self.cr_c_90 = self._castToFloat(row[142]) 
        self.goals_outside_box = self._castToFloat(row[143]) 
        self.hdrs_l_90 = self._castToFloat(row[144]) 
        self.k_tck_90 = self._castToFloat(row[145]) 
        self.op_cr_pct = self._castToFloat(row[146]) 
        self.op_crs_a_90 = self._castToFloat(row[147]) 
        self.op_crs_c_90 = self._castToFloat(row[148]) 
        self.ps_a_90 = self._castToFloat(row[149]) 
        self.shts_blckd_90 = self._castToFloat(row[150]) 
        self.shots_outside_box_90 = self._castToFloat(row[151]) 
        self.xg_90 = self._castToFloat(row[152]) 
        self.saves_90 = self._castToFloat(row[153]) 
        self.inf = self._castToFloat(row[154]) 
        self.rec = self._castToFloat(row[155]) 

    def isCenterBack():
        return False
    
    def isWingBack(self):
        return ('D' in self.position or 'WB' in self.position) and any(x in self.position for x in ('R', 'L', 'RL'))
    
    def isDefensiveMid():
        return False
    
    def isAttackingMid():
        return False
    
    def isWinger():
        return False
    
    def isStriker():
        return False

    def getData(self):
        return self.__dict__
    
    def _canCastToFloat(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False
    
    def _castToFloat(self, value):
        try:
            if '%' in value:
                value = value.replace('%', '')
            if value.endswith('mi'):
                value = value.replace('mi', '')
            if value.endswith('p/w'):
                value = value.replace('p/w', '')
            if ',' in value:
                # Locales do not matter as this will always be ENG/UK 
                value = value.replace(',', '')
            # if '£' in value:
            #     value = value.replace('£', '')
            if value == '-':
                # If we do not know the value, we can't work out their score from it, so zero allows us to not account for it.
                value = 0
            return float(value) if isinstance(value, (int, float, str)) and self._canCastToFloat(value) else value
        except ValueError:
            return value
    
    def _attributeMasking(self, value):
        if '-' not in value:
            return int(value)
        
        if value == '-':
            return 0
        
        values = [int(num) for num in value.split('-')]

        return int(sum(values) / len(values))

    def getScore(self):
        with open('weights.json') as file:
            data = json.load(file)

            return round((
                ((self.wor + self.tea) * data['work']) + 
                ((self.acc + self.pac + self.nat + self.sta) * data['speed']) + 
                ((self.dec + self.com + self.otb + self.det) * data['finishing']) + 
                ((self.fin + self.fir + self.drb) * data['technical'])
            ) / 4, 2)
        
    def getValue(self) -> float:
        return 0
        # if self.transfer_value == "Not for Sale" or self.transfer_value == 'Unknown':
        #     return 1000000000
        
        # self.transfer_value = self.transfer_value.replace('M', '000000')
        # self.transfer_value = self.transfer_value.replace('K', '000')
        # if '-' not in self.transfer_value:
        #     return float(self.transfer_value.replace('£', '').replace('M', ''))
        
        # value = self.transfer_value.replace('£', '').replace('M', '')

        # return sum([float(num) for num in value.split('-')])
        # # return 0
        

        