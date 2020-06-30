# /usr/bin/env python
# -*- coding -*-: utf-8
# software: sublime-text3
# date: 2020/06/30
# description: this is a python file to produce a molecule position and mass.
# author: ddw20191222
# email: ddw2019@mail.ustc.edu.cn
# name: diblock_module.py

import re
import sys
import string
import os

class Atom_class():
	'''
	Atom class
	'''
	def __init__(self, RecordName='ATOM', AtomSerial = 0, AtomName = 'AN', AlterLocationIndicator ='', 
		ResidueName = 'RN', ChainIdentifier = '', ResidueSerial = 1, CodeForInsertionsOfResidues = '', 
		AtomCoorX = 0.0, AtomCoorY = 0.0, AtomCoorZ = 0.0,
		Occupancy = 1.0, TempFactor = 0.0, SegmentIndent = '', ElementSymbol = '', Charge = ''
		):
		self.RecordName = RecordName
		self.AtomSerial = AtomSerial
		self.AtomName = AtomName
		self.AlterLocationIndicator = AlterLocationIndicator
	
		self.ResidueName = ResidueName
		self.ChainIdentifier = ChainIdentifier
		self.ResidueSerial = ResidueSerial
		self.CodeForInsertionsOfResidues = CodeForInsertionsOfResidues
	
		self.AtomCoorX = AtomCoorX
		self.AtomCoorY = AtomCoorY
		self.AtomCoorZ = AtomCoorZ 
	
		self.Occupancy = Occupancy
		self.TempFactor = TempFactor
		self.SegmentIndent = SegmentIndent
		self.ElementSymbol = ElementSymbol
		self.Charge = Charge


	def atom_2_PDBFormat(self):
		s = "{:6s}{:5d}{:4s}{:1s}\
		{:3s}{:1s}{:4d}{:1s}\
		{:10.3f}{:10.3f}{:10.3f}\
		{:6.2f}{:6.2f}\
		{:4s}{:2s}{:2s}\
		".format(self.RecordName.ljust(6), self.AtomSerial, self.AtomName, self.AlterLocationIndicator,\
			self.ResidueName, self.ChainIdentifier, self.ResidueSerial, self.CodeForInsertionsOfResidues,\
			self.AtomCoorX, self.AtomCoorY, self.AtomCoorZ,\
			self.Occupancy, self.TempFactor,\
			self.SegmentIndent, self.ElementSymbol, self.Charge)
		return s

def Atom_2_PSF(atomHead = 'ATOM', atomSerial = 0, atomName = 'NN', atomType = 'NN', Mass = 0.0, Charge = 0.0, Unset = 0.0):
	'''
	Template:
	ATOM 	1 	OA 	`OA 	31.0337 	0.00 	0.0
	OUT E.G.:
	ATOM 	0 	NN	 NN 	 0.0000 	0.00`	0.0
	'''
	s = "{:4s}{:8d}{:8s}{:12s}\
	{:15.4f}{:8.2f}{:8.1f}".format(atomHead, atomSerial, atomName, atomType, \
		Mass, Charge, Unset)
	return s

def Bond_2_PSF(bondHead='BOND', bondSerial=0, bondTypeSerial=0, bondIndex1=0, bondIndex2=0, bondIndex1Type='NN', bondIndex2Type='NN'):
	'''
	TEMPLATE:
	BOND    1    1    1    2   OA  EO
	OUT.E.G.
	BOND    1    1    1    2   A1  A2
	'''
	s = "{:5s} \
	{:5d}{:5d}{:5d}{:5d}\
	{:5s}{:5s}".format(bondHead, 
		bondSerial, bondTypeSerial, bondIndex1, bondIndex2, 
		bondIndex1Type, bondIndex2Type)
	return s

def Angle2PSF(angleHead='ANGLE', angleSerial=0, angleTypeSerial=0, angleIndex1=0, angleIndex2=0, angleIndex3=0, angleIndex1Type='NN', angleIndex2Type='NN', angleIndex3Type='NN') :
	'''
	TEMPLATE:
	ANGLE   1    1    1    2   3   OA  EO  EO
	OUT E.G.
	ANGLE   0    0    0    0    0   NN  NN  NN
	'''
	s = "{:5s} \
	{:5d}{:5d}{:5d}{:5d}{:5d}\
	{:5s}{:5s}{:5s}".format(angleHead,
	angleSerial, angleTypeSerial, angleIndex1, angleIndex2, angleIndex3, 
	angleIndex1Type, angleIndex2Type, angleIndex3Type
		)
	return s
def WritePDB():
	'''
	OUT E.G.  ATOM      0   AN  RN     1       0.000   0.000   0.000  1.00  0.00
	TEMPLATE. ATOM     17  NE2 GLN     2      25.562  32.733   1.806  1.00 19.49      1UBQ  87
	'''
	RecordName="ATOM"
	AtomSerial=0
	AtomName="AN"
	AlterLocationIndicator=""
	ResidueName="RN"
	ChainIdentifier=""
	ResidueSerial=1
	CodeForInsertionsOfResidues=""
	AtomCoorX=0.0
	AtomCoorY=0.0
	AtomCoorZ=0.0
	Occupancy=1.0
	TempFactor=0.0
	SegmentIndent=""
	ElementSymbol=""
	Charge=""
	TempAtom = ""

	if re.match('^\d', AtomName) != None:
		TempAtom = AtomName.ljust(4)
	elif len(AtomName) < 4:
		TempAtom = (' ' + AtomName).ljust(4)
	else:
		TempAtom = AtomName

	s = "{:6s}{:5d}{:5s}{:1s}\
	{:3s}{:1s}{:4d}{:1s}\
	{:8.3f}{:8.3f}{:8.3f}{:6.2f}{:6.2f}\
	{:4s}{:2s}{:2s}".format(RecordName.ljust(6), AtomSerial, AtomName, AlterLocationIndicator, \
				  ResidueName, ChainIdentifier, ResidueSerial, CodeForInsertionsOfResidues,\
				  AtomCoorX, AtomCoorY, AtomCoorZ, \
				  Occupancy, TempFactor, \
				  SegmentIndent, ElementSymbol, Charge)
	print(s)

if __name__=="__main__":
	WritePDB()
	b = Atom_class(AtomSerial=0, AtomName="AN", ResidueName="RN", ResidueSerial=1, AtomCoorX=0.0, AtomCoorY=0.0, AtomCoorZ=0.0,)
	c = b.atom_2_PDBFormat()
	print(c)
	d = Atom_2_PSF()
	print(d)
	e = Bond_2_PSF()
	print(e)
	f = Angle2PSF()
	print(f)