import gzip, os
from glob import glob

class Fort10(object):
  fields=[
  ('turn_max', 'int', 'Maximum turn number'),
  ('sflag', 'int', 'Stability Flag (0=stable', '1=lost)'),
  ('qx', 'float', 'Horizontal Tune'),
  ('qy', 'float', 'Vertical Tune'),
  ('betx', 'float', 'Horizontal beta-function'),
  ('bety', 'float', 'Vertical beta-function'),
  ('sigx1', 'float', 'Horizontal amplitude 1st particle'),
  ('sigy1', 'float', 'Vertical amplitude 1st particle'),
  ('deltap', 'float', 'Relative momentum deviation Deltap'),
  ('dist', 'float', 'Final distance in phase space'),
  ('distp', 'float', 'Maximumslope of distance in phase space'),
  ('qx_det', 'float', 'Horizontal detuning'),
  ('qx_spread', 'float', 'Spread of horizontal detuning'),
  ('qy_det', 'float', 'Vertical detuning'),
  ('qy_spread', 'float', 'Spread of vertical detuning'),
  ('resxfact', 'float', 'Horizontal factor to nearest resonance'),
  ('resyfact', 'float', 'Vertical factor to nearest resonance'),
  ('resorder', 'int', 'Order of nearest resonance'),
  ('smearx', 'float', 'Horizontal smear'),
  ('smeary', 'float', 'Vertical smear'),
  ('smeart', 'float', 'Transverse smear'),
  ('sturns1', 'int', 'Survived turns 1st particle'),
  ('sturns2', 'int', 'Survived turns 2nd particle'),
  ('sseed', 'float', 'Starting seed for random generator'),
  ('qs', 'float', 'Synchrotron tune'),
  ('sigx2', 'float', 'Horizontal amplitude 2nd particle'),
  ('sigy2', 'float', 'Vertical amplitude 2nd particle'),
  ('sigxmin', 'float', 'Minimum horizontal amplitude'),
  ('sigxavg', 'float', 'Mean horizontal amplitude'),
  ('sigxmax', 'float', 'Maximum horizontal amplitude'),
  ('sigymin', 'float', 'Minimum vertical amplitude'),
  ('sigyavg', 'float', 'Mean vertical amplitude'),
  ('sigymax', 'float', 'Maximum vertical amplitude'),
  ('sigxminld', 'float', 'Minimum horizontal amplitude (linear decoupled)'),
  ('sigxavgld', 'float', 'Mean horizontal amplitude (linear decoupled)'),
  ('sigxmaxld', 'float', 'Maximum horizontal amplitude (linear decoupled)'),
  ('sigyminld', 'float', 'Minimum vertical amplitude (linear decoupled)'),
  ('sigyavgld', 'float', 'Mean vertical amplitude (linear decoupled)'),
  ('sigymaxld', 'float', 'Maximum vertical amplitude (linear decoupled)'),
  ('sigxminnld', 'float','Minimum horizontal amplitude (nonlinear decoupled)'),
  ('sigxavgnld', 'float', 'Mean horizontal amplitude (nonlinear decoupled)'),
  ('sigxmaxnld', 'float','Maximum horizontal amplitude (nonlinear decoupled)'),
  ('sigyminnld', 'float', 'Minimum vertical amplitude (nonlinear decoupled)'),
  ('sigyavgnld', 'float', 'Mean vertical amplitude (nonlinear decoupled)'),
  ('sigymaxnld', 'float', 'Maximum vertical amplitude (nonlinear decoupled)'),
  ('emitx', 'float', 'Emittance Mode I'),
  ('emity', 'float', 'Emittance Mode II'),
  ('betx2', 'float', 'Secondary horizontal beta-function'),
  ('bety2', 'float', 'Secondary vertical beta-function'),
  ('qpx', 'float', "Q'x"),
  ('qpy', 'float', "Q'y"),
  ('dum1', 'float', 'Dummy1'),
  ('dum2', 'float', 'Dummy2'),
  ('dum3', 'float', 'Dummy3'),
  ('dum4', 'float', 'Dummy4'),
  ('dum5', 'float', 'Dummy5'),
  ('dum6', 'float', 'Dummy6'),
  ('dum7', 'float', 'Dummy7'),
  ('int1', 'float', 'Internal1'),
  ('int2', 'float', 'Internal2')]