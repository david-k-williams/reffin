import 'package:flutter/material.dart';
import 'package:reffin_industries/reffin_industries.dart';

void main() {
  runApp(const IndustriesExampleApp());
}

class IndustriesExampleApp extends StatelessWidget {
  const IndustriesExampleApp({super.key});

  @override
  Widget build(BuildContext context) {
    final software = resolveIndustry('513210')!;
    final manufacturingSubsectors = childrenOf('31-33');
    final wheat = resolveSic('0111')!;

    return MaterialApp(
      theme: ThemeData(useMaterial3: true),
      home: Scaffold(
        appBar: AppBar(title: const Text('Industry reference data')),
        body: ListView(
          children: [
            ListTile(
              leading: Icon(software.icon),
              title: Text('${software.code}: ${software.title}'),
              subtitle: Text('${software.sector.label} / parent ${software.parent!.code}'),
            ),
            ListTile(
              leading: Icon(IndustrySector.manufacturing.icon),
              title: const Text('31-33: Manufacturing'),
              subtitle: Text('${manufacturingSubsectors.length} direct subsectors'),
            ),
            ListTile(
              leading: Icon(wheat.icon),
              title: Text('${wheat.code}: ${wheat.title}'),
              subtitle: Text('Historical SIC / ${wheat.division.label}'),
            ),
          ],
        ),
      ),
    );
  }
}
