# .NET / C# Example

Suggested sequence:
`dotnet restore → NuGet audit/ecosystem SCA → CodeQL/SonarQube/Roslyn analyzers → dotnet test → dotnet publish → image scan → SBOM → sign → staging → DAST`.
