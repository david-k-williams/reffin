// Generated CategoryPurposeCode. Do not edit by hand.
// Input SHA-256: 19974f774033233e47b53dfeac096702fba546f42352d85cceb0192845d89b80
// ignore_for_file: require_trailing_commas
part of 'generated.dart';

enum CategoryPurposeCode {
  bonu('BONU'),
  cash('CASH'),
  cblk('CBLK'),
  ccrd('CCRD'),
  cdis('CDIS'),
  cgwv('CGWV'),
  cipc('CIPC'),
  conc('CONC'),
  cort('CORT'),
  cpay('CPAY'),
  cryp('CRYP'),
  ctdf('CTDF'),
  dcrd('DCRD'),
  divi('DIVI'),
  dvpm('DVPM'),
  epay('EPAY'),
  fcdt('FCDT'),
  fcin('FCIN'),
  fcol('FCOL'),
  govt('GOVT'),
  gp2p('GP2P'),
  hedg('HEDG'),
  iccp('ICCP'),
  idcp('IDCP'),
  intc('INTC'),
  inte('INTE'),
  lbox('LBOX'),
  loan('LOAN'),
  mp2b('MP2B'),
  mp2p('MP2P'),
  othr('OTHR'),
  pens('PENS'),
  rpre('RPRE'),
  rrct('RRCT'),
  rvpm('RVPM'),
  sala('SALA'),
  savg('SAVG'),
  secu('SECU'),
  ssbe('SSBE'),
  supp('SUPP'),
  swep('SWEP'),
  taxs('TAXS'),
  topg('TOPG'),
  trad('TRAD'),
  trea('TREA'),
  vatx('VATX'),
  vost('VOST'),
  whld('WHLD'),
  zaba('ZABA');

  const CategoryPurposeCode(this.code);
  final String code;
  Iso20022CodeInfo get info => resolveCode('ExternalCategoryPurpose1Code', code)!;
  String get label => info.label;
  IconData get icon => info.icon;
  static CategoryPurposeCode? tryParse(String code) =>
      _categoryPurposeByCode[_key(code)];
}

final Map<String, CategoryPurposeCode> _categoryPurposeByCode = Map.unmodifiable(<String, CategoryPurposeCode>{
  for (final value in CategoryPurposeCode.values) _key(value.code): value,
});
